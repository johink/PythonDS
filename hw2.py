"""HOMEWORK TWO"""
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()

#np.c_ is basically performing a cbind here of both the data and the class label
iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

#%%

"""Q1
PLOTTING IN PANDAS AND MATPLOTLIB

Iris is a dataset containing information about flowers
For more information about this information about flowers, please visit this link: https://en.wikipedia.org/wiki/Iris_flower_data_set

The Iris dataset is easy to analyze, so let's dig in!
"""

#Plot a histogram of sepal length
#Use iris.columns if you forget exactly what the column names are


#Plot a histogram of sepal length, grouped by the target variable


#Create a scatter plot of petal length vs. petal width


#Create a 3d scatter plot of petal length, petal width and the target label
#Remember to use %matplotlib qt if you want to be able to rotate the picture


#Create boxplots of all variables except target



#%%

"""Q2
RETRIEVING, IMPORTING AND ANALYZING DATA FROM THE INTERNET
"""
import requests, json

#Download the JSON file located at https://data.cityofnewyork.us/api/views/25th-nujf/rows.json?accessType=DOWNLOAD
#This file contains baby names chosen by New York parents over the span of several years.
#The data contains the year of the child's birth, the child's gender, the mother's race, the child's name, and the number of children who fit all of the previous criteria
#Retrieve the data from the provided URL


#Analyze the raw data you get back, and convert it to a dictionary


#Subset the dictionary and remove any parts you think are unnecessary.  Remember that the .keys() function will give you the names of all the keys in the dictionary
#and that you can pretty print the JSON to get a better understanding of its structure

#Convert your dictionary into a pandas DataFrame.  Make sure each column is the proper type, as all variables have been retrieved from the internet as strings.


#Now that you've got a cleaned-up dataset, answer the following questions:
#What is the most popular name for all years combined?


#What is the most popular name by year, race, and gender?  Remember that you can groupby using multiple columns,
#and that summary statistics like max and min are called using .max() and .min().  If confused, please reference the pandas practice script!


#Does there seem to be any trend regarding the first letter of a baby's name by gender?  By race?  Try creating a bar chart to prove one way or the other


"""Q3
USING A DATABASE WITH SQLALCHEMY
"""
import sqlalchemy

#Start your WAMPServer and connect to it using SQLAlchemy, then write a query to select the following from the products database we used in our SQL project:
#Salesperson | Customer | OrderNumber | Product | Quantity | Price


#Read the results into a pandas DataFrame, and then conduct the following analysis:
#Which salesperson has the most sales?  Which customer has purchased the most?


#Which order was the largest?  What was its dollar amount, what items were purchased, and how many of them were purchased?


#How many items have we sold in total?  Which product is our best seller by quantity sold?  Which product is best by total revenue generated?


#For each salesperson, which products have they never sold to a customer?


