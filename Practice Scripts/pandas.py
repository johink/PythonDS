"""PANDAS"""
#Pandas has two important data structures:  Series and DataFrame.
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#Read in mtcars
mtcars = pd.read_csv("c:/users/john/desktop/python course/pythonds/Week2/mtcars.csv")
#%%

"""SLICING EXAMPLES"""
#Get rows 10 through 14, and column mpg
mtcars[10:15]["mpg"]

#Please note that when you slice just one column, you get a Series back instead of a DataFrame
type(mtcars[10:15]["mpg"])

#Get column am, then only keep rows where vs is 0
mtcars["am"][mtcars.vs == 0]

#Get cars with a mpg > 20, and keep only the name and mpg columns
mtcars[mtcars.mpg > 20][["Unnamed: 0", "mpg"]]

#%%
"""TIME-SERIES, DATE FUNCTIONS & OFFSETS"""
"""Offset aliases are used frequently in pandas' time-series and date functions:
L 	milliseconds
S 	seconds 
T 	minutes 
H 	hours
B 	business days (ignores weekends and holidays)
D 	calendar days 
W 	weekly 
MS 	month start 
M 	month end 
SMS 	semi-month start (1st and 15th)
SM 	semi-month end (15th and end of month)
QS 	quarter start 
Q 	quarter end 
AS 	year start 
A 	year end 

You can combine these, and prefix them with numbers, so 3D30T would be 3 days and 30 minutes
These are not case-sensitive
"""
#date_range() is similar to the range() function
#It takes a starting date, a number of periods, and the "step" or interval between periods, called freq
#These frequencies are from the offset charts above
pd.date_range('1/1/2016', periods=366, freq='3d30t')

#Let's use this date_range function to make up some stock data!
STCK = Series(np.random.normal(200, 20,390), index = pd.date_range("9:30:00", periods=390, freq="min"))
STCK.plot() #That is one volatile stock!

#Maybe instead of looking at the data minute-by-minute, we want it on an hourly scale
#Enter .resample()!  It's kind of like groupby() for time-series data
#It only takes one argument: the new baseline time period
hourly = STCK.resample("H")

#With this new resampled data, you can call any aggregate functions, or create your own using agg()
#Here is a really cool provided function, which shows the open / high / low / close prices during the period
hourly.ohlc()
hourly.median()
hourly.agg({"Range":lambda x: max(x) - min(x)})


"""FUNCTIONS ON SERIES AND DATAFRAMES"""
#Series and DataFrame have many functions that they can call
#Things that work on both:
#Plotting is very powerful.  You can use .plot(kind = "kind") or .plot.kind()
#Available kinds include line, bar, bar(stacked = True), barh, hist, box, density, area, pie, scatter, hexbin
mtcars.plot(kind = "scatter", x = "mpg", y = "hp")
mtcars.plot.scatter("mpg","hp")
mtcars["cyl"].value_counts().plot.bar()

#describe() is the same thing as R's summary() function
mtcars.describe()

#concat() works on both Series and DataFrame objects
#concat() takes a list of either Series or DataFrames and returns a single Series or DataFrame of them all rbinded together
pd.concat([mtcars.mpg, mtcars.hp])

#In addition to concat(), you can also merge(), which is very similar to a join in SQL
adf = DataFrame({"ID":[100, 101, 102, 103], "Name":["Jerry","Jory","Jirry","Jarry"]})
bdf = DataFrame({"ID":[101, 102, 103, 104], "Sales":[5000, 3000, 2000, 8000]})
#Without any additional arguments, it just performs an inner join
adf.merge(bdf)
adf.merge(bdf, how = "left", left_on = "ID", right_on = "ID")

#sample() can be called directly on a Series or DataFrame
#sample() takes the sample size, with or without replacement, and allows weights to be specified for selection probability
mtcars.sample(3, replace = False)

#Here we assign the weights by the "am" column, so we only get foreign cars back
#(for some reason, a value of 1 in "am" was coded to mean non-American cars)
#Since American cars have 0 in the "am" column, then they have 0 probability of being chosen in the sample
mtcars.sample(10, replace = False, weights = "am")

#Many functions are available to be called on a Series or DataFrame
#pct_change, cov, corr, rank, sum, max, min, mean, median, quantile, std, var, skew, kurt, cumsum
#Additionally, you can create a rolling object on a Series or DataFrame using .rolling()
#rolling() takes one argument, the "window" for the roll
roll = mtcars["mpg"].rolling(3)

#You can call almost all of the above functions using this rolling window
#This basically gives you the result of the function over the window you have defined
roll.sum() #This sums the current observation and the two previous
roll.max()
roll.mean()

#Additionally, you can do the same thing with an exponential smoothing model using .ewm()
#Exponential smoothing models are like rolling windows, but observations are no longer equally weighted
smooth = mtcars["mpg"].ewm(3)
smooth.mean()

#%%
#Things that work on only Series:
mtcars["am"].value_counts() #Find the unique values and the number of occurrences of those values
  
#Sometimes you have a column which contains strings that represent categories
#For example, in the movie dataset, we had a column called genres that had values like "Drama|Comedy|Crime"
#In order to split these strings out into their respective dummy variables, you can use the str.get_dummies() function
#get_dummies() only takes one argument: the character which delineates the categories
movie_genres = ["Drama|Comedy|Crime","Fantasy|Drama","Comedy|Fantasy","Cartoon|Comedy"]
myseries = Series(movie_genres)
myseries.str.get_dummies("|")

#Sometimes you want to bin continuous data to really get on Pinder's nerves
#The pd.cut() function has you covered!
pd.cut(mtcars.mpg, range(10,40,5))

#You can even give it custom labels to make Boone happy too!
labels = ["{} to {}".format(i, i+4) for i in range(10,35,5)]
pd.cut(mtcars.mpg, range(10,40,5), labels = labels)

#%%
#Things that work on only DataFrame:
#groupby is very similar to SQL's GROUP BY clause
mtcars.groupby("gear") #What in the world is a pandas.core.groupby.DataFrameGroupBy object?

#To see what groupby actually does, let's iterate over its results and print their contents
for item in mtcars.groupby("gear"):
  print(item)
  
#groupby basically performs the same functionality as "split" in R
#It returns a list of tuples, where the first value in the tuple is the value of the groupby variable
#and the second value of the tuple is the DataFrame containing all observations which matched that value

#groupby can be followed up with an aggregate() or agg(), which is very similar to what aggregate functions (count, sum, max, avg) do in SQL
#except in Python, you can use pretty much any function you want to aggregate, including a user-defined one
mtcars.groupby("gear").aggregate([sum,max,min, lambda x: max(x) - min(x)])

#Note how groupby / aggregate threw away any columns that didn't make sense with the functions we aggregated by
#For example, look at what we have if all we do is sum and max
mtcars.groupby("gear").agg([sum, max]) #sum decided to add together all the car names (+) while max gave back the car that comes last alphabetically

#Also note that after performing groupby and aggregate, the result is a new DataFrame
type(mtcars.groupby("gear").agg([sum, max]))

#Finally, if you want to name the aggregated columns, just pass the functions in a dictionary
#Also, you can groupby multiple columns at once
mtcars.groupby(["am","vs"]).agg({"mpg":{"total":np.mean,"biggest":max},"hp":{"median":np.median,"smallest":min}})

#You can create cross-tabulations (confusion matrices) using the pd.crosstab() function
pd.crosstab(mtcars.am, mtcars.vs)

#You can also add margins and normalize the values to proportions
pd.crosstab(mtcars.am, mtcars.vs, margins = True, normalize = True)

#%%
#Dropping rows/columns can be done with the .drop() function
#drop() takes the names of things to drop, and the axis to drop from (0 = row, 1 = col)
mtcars.drop(["vs","am"], 1) #Be careful!  drop() does not modify the DataFrame itself, but instead returns a new DataFrame without the dropped parts
mtcars.drop(range(5,15), 0)

#There is another version called dropna(), which drops rows / columns with NAs
#dropna() takes the axis to drop from (0 = row, 1 = col), and a criteria of "any" or "all"
#"any" says drop the row/column if even a single value is NA, while "all" requires all values to be NA in the row/column for it to be dropped
#Make sure you do mtcars.copy() and not just mtcars.  mtcopy = mtcars just means that both variables now point to the same DataFrame!
mtcopy = mtcars.copy()
mtcopy.carb = np.NaN
mtcopy.dropna(1, "all")
#%%
"""DATAFRAME INDICES"""
#DataFrame indices are basically the same thing as row labels in R
#If we look at mtcars, we can see the index is a range from 0 to 31
mtcars

#To get or set index values, use .index
#Get indices
mtcars.index

#Set indices
mtcars.index = range(2,34,1)

#Now you can see the numbers are offset by 2
mtcars[5:10]

#If you screw up your index, there is always the reset_index() function
mtcars.reset_index()

#This might seem kinda pointless, but sometimes the index carries useful information.
#For example, instead of being an incremental number, the index could contain a timestamp for time-series data
#set_index() can be used to set a column (or columns) as the new index
mtcars.set_index("Unnamed: 0") #Now the car name is the row identifier!