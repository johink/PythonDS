"""CSV & VISUALIZATION EXERCISE"""
#Let's read in the mtcars dataset
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #Axes3D allows us to choose "3d" as a projection type

#There are different styles available:
matplotlib.style.use("ggplot")

#Load the dataset
mydf = pd.read_csv("week2/mtcars.csv")

#Check out the first six rows
mydf.head()

#inline graphics appear "in-line" in the IPython window
%matplotlib inline

#%%
#You can easily make histograms and 2d plots with pandas:
#Here we subset the dataframe and grab only the mpg column, then
#call plot.hist() on it
mydf.mpg.plot.hist()

#%%
#Here we subset down to a two column dataframe:
mydf[["cyl","carb"]].plot.hist(alpha = .6)
#With changing the alpha, the spots where the bars are stacked
#blend their colors

#%%
#Too many variables gets kind of meaningless...
mydf.plot.hist(alpha =.3)

#%%

#Scatterplots are similarly easy:
mydf.plot.scatter("hp","mpg")

#%%

#plot.box() will plot all variables passed to it
mydf.plot.box()

#but you can always subset
mydf[["mpg","hp","cyl"]].plot.box()

#%%
#pandas is convenient, but can't really handle 3d plots
#Luckily, we have matplotlib

#qt makes graphics appear in a separate window
%matplotlib qt

#First, we create a new figure
fig = plt.figure(1)

#Then, we add a new axis to the figure
#111 indicates that there only exists one row and one column in 
#this figure, and we're getting a reference to the first subplot in "ax"
ax = fig.add_subplot(111, projection="3d")

#Set the labels of the axis
ax.set_xlabel("Horsepower")
ax.set_ylabel("# Cylinders")
ax.set_zlabel("Miles Per Gallon")

#Add scatterplots to the axis
#c refers to color, marker refers to the type of dot
ax.scatter(mydf.hp, mydf.cyl, mydf.mpg, c="b", marker="^")

#Show all plots
plt.show()

#%%
