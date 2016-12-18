"""LINEAR ALGEBRA"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

%matplotlib qt5
#Read in the file with RGB encoding
pic = imread("Week4/hello.data", mode = "RGB")

#It's a numpy array!
type(pic)

#.shape tells us the dimensions.  Note this is a 3d array.
pic.shape
length, width, depth = pic.shape

#matplotlib.pyplot.imshow() is a convenient way to show a picture
plt.imshow(pic)

#%%
#Let's do some random stuff and see how it affects the picture!
#Add/subtract/multiply/divide:
plt.imshow(pic+20)
plt.imshow(pic-20)
plt.imshow(pic/2)
plt.imshow(pic*2)

#What if we just target certain channels?
#Remember, it's RGB:  Red, Green, Blue!
plt.imshow(pic - [20,-20,20])

#%%
#Let's use numpy slicing to mess with things
#Here we'll change the color order from RGB to BGR
plt.imshow(pic[:,:,::-1])

#Here we'll throw away every other row and column
plt.imshow(pic[::2,::2,:]) #Looks kinda blurry!

plt.imshow(pic[::4,::4,:])

plt.imshow(pic[::10,::10,:]) #We're pixel art!

#%%
#Transpose x and y axis:
plt.imshow(np.transpose(pic,[1,0,2]))

#%%
censored = np.copy(pic)
censored[185:236, 775:806, :] = 0
plt.imshow(censored)

#%%
#Here we'll define a function that will take in a picture and make a specified region blurry
def blurry(picture, topleft, bottomright, factor = 10):
  import matplotlib.pyplot as plt
  top , left = topleft
  bottom , right = bottomright
  #i refers to row dimension
  for i in range(top, bottom, factor):
    #j refers to column dimension
    for j in range(left, right, factor):
      #k refers to color dimension
      for k in range(3):
        #Take a factor by factor slice of the picture in the kth color dimension, and set all values to the mean
        picture[i:(i + factor), j:(j + factor), k] = np.mean(picture[i:(i + factor), j:(j + factor), k])
  plt.imshow(picture)

#%%
blurry(np.copy(pic), (100,450), (150,650), 4)

blurry(np.copy(pic), (185,775), (236,806), 5)

#%%
#Average together the RGB channel
grey = np.mean(pic, 2)

#Cast it back to an unsigned 8-bit integer
grey = grey.astype("uint8")

#We went from 3 dimensions to 2, so let's add back the third dimension
grey = np.array([grey,grey,grey])

#Looks like the dimensions are out of order
grey.shape

#Let's plot it after transposing to be the correct dimensions again
plt.imshow(np.transpose(grey, [1,2,0]))

#%%
#Also, if you plot just the results of the mean, you get something pretty cool!
#From looking at the numbers, apparently if there is only one channel then it serves as a sliding scale
#Very high numbers are red, very low numbers are blue, and numbers towards the middle are greenish.
#But how do colors have high/low numbers originally?  What is this transformation doing?
plt.imshow(np.mean(pic, 2))

#%%
#Let's reshape the data
#Here I've basically doubled the number of rows by splitting each column in half and interpolating them
plt.imshow(np.reshape(pic, (972, 480, 3)))

#%%
#PCA example with 3d plots
from sklearn.decomposition import PCA
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import pandas as pd
import numpy as np

basedf = pd.read_csv("Week2/mtcars.csv")

#We'll add a new column for example purposes later, and drop the names column
basedf["useless"] = 25
mydf = basedf.drop("Unnamed: 0", 1)

#Before we conduct PCA, we must normalize our data.
#This is because PCA places the most emphasis on the thing with the most variance, which can be exaggerated when things are scaled differently
#For example, on which dimension do you believe Alex and Bob differ more?
#Alex is 31 years old and makes $75,000 per year
#Bob is 67 years old and makes $73,000 per year

#To normalize data, it is common to subtract the mean and divide by the std
#Here we use the apply function to apply this independently to all columns
mydf = mydf.apply(lambda x: (x - x.mean()) / x.std())

#Oops!  Since the "useless" column had a std of 0, we ended up with a bunch of NaNs
mydf.useless = 0

#%%
#Now we're ready to PCA!
#Here we instantiate the PCA object, which we can use to conduct PCA.
#n_components indicates how many components we want to keep.  Here we are keeping three components
pca_object = PCA(n_components = 3)

#Here we are transforming a three-dimensional object and keeping three components, so we haven't lost any information
transformed = pca_object.fit_transform(mydf[["hp","cyl","mpg"]])

#Turn it back into a DataFrame from a numpy array
transformed = pd.DataFrame(transformed, columns = ["hp","cyl","mpg"])

#To view our eigenvectors
eigenvectors = pca_object.components_

#And our eigenvalues
eigenvalues = pca_object.explained_variance_

#If we want to see what proportion of the variation is explained by each principal component
pca_object.explained_variance_ratio_

#We can sum these values to find the proportion explained
sum(pca_object.explained_variance_ratio_) #All three: 100%
sum(pca_object.explained_variance_ratio_[:2]) #First two:  96%
pca_object.explained_variance_ratio_[0] #Just the first:  88%



#%%

#Plotting the results

#First, we create a new figure
fig = plt.figure(1)

#Here's that funky syntax again.  This is saying we want the plot space divided up into two rows and columns,
#and we want our subplot to take up the first (top-left) square
ax = fig.add_subplot(221, projection="3d")

#Set the labels of the axis
ax.set_xlabel("Horsepower")
ax.set_ylabel("# Cylinders")
ax.set_zlabel("Miles Per Gallon")
ax.set_title("Untransformed Data")

ax.scatter(basedf.hp, basedf.cyl, basedf.mpg, c="b", marker="^")

ax = fig.add_subplot(222, projection="3d")

#Set the labels of the axis
ax.set_xlabel("Horsepower")
ax.set_ylabel("# Cylinders")
ax.set_zlabel("Miles Per Gallon")
ax.set_title("Normalized Data")

#Add scatterplots to the axis
#c refers to color, marker refers to the type of dot
ax.scatter(mydf.hp, mydf.cyl, mydf.mpg, c="g", marker="x")

#Divide the plot space into two rows and two columns, then give me the area where the third (bottom-left) is
ax = fig.add_subplot(223, projection="3d")

#Set the labels of the axis
ax.set_xlabel("Axis 1")
#Set the x-axis named "Axis 1" to green
plt.xlabel("Axis 1").set_color("green")
ax.set_ylabel("Axis 2")
plt.ylabel("Axis 2").set_color("red")
ax.set_zlabel("Axis 3")
ax.set_title("PCA Data")

ax.scatter(transformed["hp"], transformed["cyl"], transformed["mpg"], c="r", marker="o")


ax = fig.add_subplot(224, projection="3d")

#Set the labels of the axis
ax.set_xlabel("Horsepower")
ax.set_ylabel("# Cylinders")
ax.set_zlabel("Miles Per Gallon")
ax.set_title("Normalized Data w/ PCA Axes")

#Add scatterplots to the axis
#c refers to color, marker refers to the type of dot
ax.scatter(mydf.hp, mydf.cyl, mydf.mpg, c="g", marker="x")

for vector, value, color in zip(eigenvectors, [5,3,1], ["green", "red","black"]):
  ax.plot([0,vector[0]],[0,vector[1]],[0,vector[2]], c=color, linewidth = value)

for vector in eigenvectors:
  ax.scatter(vector[0],vector[1],vector[2], c="black", marker="o")
  
#Show all plots
plt.show()

#%%
#I broke that into four separate pieces above, but one of the most important concepts in programming is DRY - Don't Repeat Yourself
#We should write a function, a class, or a for loop which can reduce the amount of typing
#Here's an example doing (pretty much) the above with a for loop
import numpy as np
cols = ["hp","cyl","mpg"]
the_data = [basedf[cols], mydf[cols], transformed, mydf[cols]]
titles = ["Untransformed Data","Normalized Data", "PCA Data","Normalized Data w/ PCA Axes"]

fig = plt.figure(1)
for data, title, i, tick, color in zip(the_data, titles, range(4), ["^","x","o","x"], ["b","g","r","g"]):
  ax = fig.add_subplot(221 + i, projection="3d")
  ax.set_xlabel("Horsepower")
  ax.set_ylabel("# Cylinders")
  ax.set_zlabel("Miles Per Gallon")
  ax.set_title(title)
  
  ax.scatter(np.array(data)[:,0], np.array(data)[:,1], np.array(data)[:,2], c=color, marker=tick)

  if i == 3:
    for vector, value, color in zip(eigenvectors, [5,3,1], ["green", "red","black"]):
      ax.plot([0,vector[0]],[0,vector[1]],[0,vector[2]], c=color, linewidth = value)
    
    for vector in eigenvectors:
      ax.scatter(vector[0],vector[1],vector[2], c="black", marker="o")

      
#Okay, maybe that wasn't that much faster.  But imagine if you had 100 things to plot!


#%%      
#However, PCA is usually used for dimensionality reduction
#Let's convert all the columns except mpg into at most 5 components
pca_object = PCA(n_components = 5)

#Here we are transforming a three-dimensional object and keeping three components, so we haven't lost any information
transformed = pca_object.fit_transform(mydf.drop("mpg", 1))

#If we want to see what proportion of the variation is explained by each principal component
pca_object.explained_variance_ratio_

#Now we have distilled 11 dimensions from mydf into 5 PCA dimensions
pca_object.explained_variance_ratio_[0] #Just the first:  58%
sum(pca_object.explained_variance_ratio_[:2]) #First two:  84%
sum(pca_object.explained_variance_ratio_[:3]) #First three:  90%
sum(pca_object.explained_variance_ratio_[:4]) #First four:  93%
sum(pca_object.explained_variance_ratio_) #All five: 95%

#From this analysis, we can reduce our dimensionality from 11 to 3 and only lose 10% of the information in the dataset!


#%%
#Food for thought:  [0 1; 1 1] matrix to the nth power
#np.dot() gives you matrix multiplication
mystery = np.array([[0,1],[1,1]])

np.linalg.eig(mystery)
