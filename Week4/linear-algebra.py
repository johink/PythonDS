"""LINEAR ALGEBRA"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

#Read in the file with RGB encoding
pic = imread("Week4/hello.data", mode = "RGB")

#It's a numpy array!
type(pic)

#.shape tells us the dimensions.  Note this is a 3d array.
pic.shape

#matplotlib.pyplot.imshow() is a convenient way to show a picture
plt.imshow(pic)
#%%
#Transpose x and y axis:
plt.imshow(np.transpose(pic,[1,0,2]))

