"""
Python first steps!

I have followed the format of Professor Rhue's first R assignment so you can
compare the content and better see the similarities and differences!

"""

###############################################################################
# BASIC OPERATIONS WITH NUMBERS
# addition 
1 + 2
# order of operations
1 * 5 + 10/100
# compare values using >, <, =
1 < 2 # returns boolean values
1 > 5
### EXERCISE ###
# There are 56040 records in the data set: 11208 contain red labels, 28020
# contain yellow labels, and the rest contain blue labels.
# 1. What is the percent with yellow labels?

# 2. What is the percent of records with blue labels?  (Write in one expression.)


###############################################################################
# Vectors don't exist in base Python
# But Pandas mimics their functionality very well!
import pandas as pd

pd.Series([1,2,2,2])

# vector addition and multiplication
pd.Series([1,2,3,4]) + pd.Series([1,2,3,2])

pd.Series([1,2,3,4]) * pd.Series([1,2,3,2]) # individual, element-wise multiplication
pd.Series([1,2,3,4]) * pd.Series([1,2,3]) # Python won't repeat the smaller vector

# In Python, if the vectors are not the same size, the vector WON'T repeat!
pd.Series([1,2,3,4]) + pd.Series([1,2])  # Two NaNs

# use range to create a vector with a particular pattern
pd.Series(range(2,10,2))

### EXERCISE ###
# Create a vector with four numbers: 3,6,10,11.


# Create a vector with two numbers: 4,56040.


# Add the two vectors together. Is this the same result as you would get in R?


# Create a sequence from 0 - 100, counting by 10.


###############################################################################
# FUNCTIONS
# f(input1, input2, ...)
import math
math.e # just a constant in Python
math.log(8) # natural log
math.log(8,2) # log base 2
3**2 # 3 squared
math.sqrt(9)

pd.Series([2,3]).mean()
pd.Series([2,3]).median()

### EXERCISE ###

# What is e^2 in Python?

# What is the log of that?

# What is the log of 0?

# What is 3234 squared?

# What is the mean of 24,100,32?


###############################################################################
# VARIABLES
# use = to assign value to variable
x = 1
y = pd.Series([1,2,3,4])
y = pd.Series(["abc","bcd","cde","def"])

#index / slice
#if the variable is not atomic, you can use brackets to access elements
#Python brackets are [start:stop)
#In other words, inclusive of start value, exclusive of stop value
y[1] #Accessing a single element returns an atomic value
y[2:4] #Slicing returns a Series

### EXERCISE ###
# Create a vector with 5 numbers [3, 5, 8, 2, 4] and assign it to y.


# Multiple each of those elements by 2 and assign it to the variable x.


# Find the 4th value in the vector x.


# What is the mean of the 2nd and 3rd value in x? (You can do this in many ways.)


###############################################################################
# types
# type of the variable: ints, floats, strings
type(1) #int:  integers represent positive or negative whole numbers
type(1.5) #float:  floats can represent non-integer values
type("stringed") #str: strings are basically words
x = pd.Series(["red","red","yellow","blue", "red"]) #string Series
x = pd.Series(["red","red","yellow","blue", "red"], dtype="category") #it's a factor!
x.cat.categories # find the unique values in the factor vector
x = pd.Series(["red","red","yellow","blue", "red"]).astype("category", categories=["yellow","orange","red"], ordered=True)
x.cat.categories # find the unique values in the factor vector


# date

newyear = pd.to_datetime("2016-01-01")

# what happens when you format the date differently?
print(pd.to_datetime("01/01/2016"))  #nothing!

# pandas' to_datetime method is very good at figuring out the format

# you can add or subtract days to the original date using DateOffset
newyear + pd.DateOffset(days=1)

type(newyear)

### EXERCISE ###
# type of the variable: numeric, character, factor, date
# Create a numeric vector with 4 values divisible by 5.


# Create a string vector with 4 values. 


# Create a factor vector with 3 values and a length 7.


# Create a date variable for July 7,2016.


# What is the date 28 days before July 7,2016?



###############################################################################
# DATA FRAMES AND MATRICES
# Two-dimensional forms of organizing data like a single spreadsheet

dat = pd.DataFrame({"id":[1,2,3,4], "cond":["A","B","C","D"]})

#Since Python won't repeat shorter vectors, this results in an error
# dat = pd.DataFrame({"id":[1,2,3,4], "cond":["A","B"]})

#boolean row slicing
dat[dat.id > 2]

#column label slicing (all rows)
dat["cond"]

#row index slicing (all columns)
dat[0:3]

#You can combine these actions:
dat["cond"][0:3]
dat[0:3]["cond"]

#These slicing methods above should serve 99% of your needs, 
#but these additional methods may be required in certain situations
#Must use a property to simultaneously slice both rows and columns
# .loc uses row and column labels
dat.loc[1:2,"id"]  #Note that .loc is *inclusive* on both sides, i.e. [start,stop]

# .iloc uses row and column indexes, this behaves like normal Python slicing
#Must use ":" if you want all rows, you can't just leave it blank like in R
dat.iloc[:,1]

#There are also extremely fast properties to access just 1 element in the DataFrame
# .at uses row and column labels
dat.at[1,"id"]

# .iat uses row and column indexes
dat.iat[2,1]

# these GET properties can also be used to SET
dat.iat[3,0] = "C"

dat.loc[1:2,"id"] = [0,2000]
dat.iloc[[0,3],1] = [500,50]

#What if the "cond" field was categorical?
dat["cond"] = dat["cond"].astype("category")

# reassign a value in the data frame
dat.iat[0,0] = "E" # Uh oh!

dat["cond"] = dat["cond"].cat.set_categories(["A","B","C","D","E"]) #return the original data but with new categories set
dat.iat[0,0] = "E" # Finally...

# access fields using the "." operator
dat.id
dat.cond

# use comparison to slice the data
dat[dat.cond=="E"]
dat.id[dat.cond=="E"]

#rename all fields with .columns
dat.columns = ["Grade","StuID"]

#rename just one field with .rename
dat.rename(columns={"Grade":"Final"}, inplace=True)

### EXERCISE ###
# Create a data frame with three fields:
#   category_id (values: 4,5,6);
#   title (values: "movies", "tv shows", "music")
#   avg_price (values: 15, 25, 2)


# Slice the data frame to find the average price of music.


# Change the average price of music to 4


# Find the name of the third field. Change that name to "mean_price".


###############################################################################
# MATRIX
# a 2x2 set of data, all values are numeric
import numpy as np
np.matrix("1 2; 3 4")
np.matrix([[1,2], [3,4]])
