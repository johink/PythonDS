""" SCOPE """
#There exists a three-tiered structure to scope in Python:
#Built-in
#  Global
#    Local

#When you use a variable, Python will first look for it in the Local environment,
#then the Global environment, and finally the Built-in environment
import pandas as pd #pandas' content is now scoped at the Built-in level
from pandas import Series #Series is now scoped at the Global level

Series = "Hello" #We have masked pandas' version of Series

type(Series)
type(pd.Series) #We can still provide the namespace to specify which "Series" we're looking for

#If your variable isn't found in any environment, an error occurs:
print(candycane)

#%%
#This means that variables you create can obscure system functionality:
alist = ["a","b","c",1,2,3]

print("len(alist) is {}".format(len(alist)))

def len(x):
    return 8000

print("len(alist) is now {}".format(len(alist)))

#Run this cell again.  What happened?

#%%
#To delete a name you've created, use the del statement
del len

#%%
#We're currently in the global environment:  let's make some variables!
x = 10
y = 5

print("In the global environment x + y = {}".format(x+y))

def add10toX(x):
    x += 10
    #Note how we can still access y's value here.  Even though y doesn't exist 
    #in the local environment, we can still find it in the global one
    print("In our local function environment x + y = {}".format(x+y))
    return

add10toX(x)

#Note how the value of x in the global environment did not change.
#Since the function returned, the x from our function is gone!
print("Back in the global environment x + y = {}".format(x+y))

#%%


"""RECURSION"""
def fib(x):
    #Base case
    if x <= 2:
        return 1
        
    #Step case
    else:
        return fib(x-1) + fib(x-2)

for x in range(1,10):
    print("Number {} in the Fibonacci Sequence is {}".format(x,fib(x)))

#%%
    

"""EXCEPTION HANDLING & VALIDATION"""
#Whenever you do something that could raise an exception, it's good practice to handle it
#Blindly trusting the user to enter correct information is generally a bad idea...
age = int(input("Please enter customer age: "))

if age >= 21:
    print("Purchase Approved")
else:
    print("Purchase Denied")
    
#%%
    
invalid = True
while invalid:
    try:
        invalid = False
        age = int(input("Please enter customer age: "))
        if age >= 21:
            print("Purchase Approved")
        else:
            print("Purchase Denied")
    except:
        invalid = True
        print("Invalid age...")

#%%
#If you'd like to have more information about the exception, you can catch it:

invalid = True
while invalid:
    try:
        invalid = False
        age = int(input("Please enter customer age: "))
        if age >= 21:
            print("Purchase Approved")
        else:
            print("Purchase Denied")
    except Exception as e:
        invalid = True
        print("Error: {}".format(e))
        
#%%
#Sometimes you'd like to differentiate between exceptions
#For example:

invalid = True
while invalid:
    try:
        x = float(input("Please enter a number: "))
        y = float(input("Please enter a second number: "))
        print ("{} / {} = {}".format(x,y,x/y))
        invalid = False;
    except ZeroDivisionError:
        print("The second number can't be zero!  Please try again.")
    except ValueError as e:
        print(e)
    finally:
        print("Finally always executes")
        
#%%
#try, except, finally is so common that the "with" statement was used to simplify
#certain access patterns
        
with open("readme.md") as file:
    for line in file:
        print(line)
        
#Notice that the variable "line" still exists, but the file connection "pic" is totally gone
        
#%%
        
"""IMPLEMENT MERGE SORT"""

#Merge sort is a recursive sorting algorithm that operates in n log n time.
#Merge sort works on the fact that it is easier to sort a bunch of tiny lists
#Rather than sorting one giant list
#Base case:  1 element list is automatically sorted
#Step case:  We will split the list in half at each point, calling merge sort on both halves,
#and then combining the returned sorted sublists
alist = [5,2,55,1,99,87,23,41,1]

def merge_sort(x):
    
    return "?"
    
    
merge_sort(alist) == sorted(alist)