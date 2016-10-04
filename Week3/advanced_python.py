"""ANONYMOUS FUNCTIONS"""

#A function which always returns 2000
(lambda:2000)()

#A function which squares its argument
(lambda x: x**2)(15)

#A function which says if its argument is even
#% is the modulus operator, also known as the "remainder" operator
#It gives you the remainder after division
(lambda x: x % 2 == 0)(6)

#A function which returns third item in a list
(lambda x: x[2])([15,25,35,45,55])

#A function which returns every other item in the list
(lambda x: x[::2])([15,25,35,45,55])

#Anonymous functions can take multiple arguments
(lambda x, y, z: x * y + z)(3,4,5)

#At this point you might be saying, "So what?"
#I agree that none of these examples are very useful, but lambda only really
#starts to shine when combined with filter, map and reduce!

#%%

"""FILTER"""
#Filter takes a function which returns True/False and filters an iterable based upon the Trues/Falses
#A very common filter function is None, which acts as an identity function and filters out falsey values
alist = ["hello",0,5.2,{},False,True,"",None,[]]
for item in filter(None, alist):
    print(item)
    
#Filter returns an iterable, not a list, so be careful!
print(filter(None, alist))

#If you want a list, use list()
print(list(filter(None, alist)))

#The same is true for dictionaries
John = {"nickname":"Johnny B","age":12,"cool?":False,"likes":["Trampoline Park","Python","Ping Pong"]}
Chase = {'nickname':'High-Speed','age':14,'cool?':True,'likes':['Ping Pong','SAS','Trampoline Park']}
Martha = {"nickname":"Top Dawson",'age':17,"cool?":True,"likes":["R",'Duke Energy',"Probably Cats?"]}
students = [John,Chase,Martha]

print(filter(lambda x: x["age"] >=13,students))

for student in filter(lambda x: x["age"] >=13, students):
    print(student["likes"])
    
#pandas implements filter-like functionality with its R-like slicing:    
import pandas as pd
mydf = pd.DataFrame(students)
mydf.loc[mydf["age"] >= 13,"likes"]
    
    
"""ITERABLES"""
#We haven't really discussed iterables before, but they're important
#Iterables are much more memory efficient than creating an entire list or dictionary
#Iterators support "lazy evaluation," which means that code is only evaluated when it's needed

#The range() function also returns an iterable
#Here's an iterable which contains the numbers 0 through 100 trillion
big_iterable = range(100000000000000)

#Look what happens when you try to fit it all into one list!
list(big_iterable)

#Python's support of iterators means you can deal with massive amounts of data without
#running out of memory

#%%
"""MAP"""
#Map applies a function across a list of inputs in parallel
#This is very useful if your data is kind of split up
#For example, calculating a weighted average
x = [5,10,15,20,25,30]
p_x = [.1,.3,.2,.05,.25,.1]

sum(map(lambda one, two: one * two, x, p_x))

#List comprehensions would not work for this!
#This is because list comprehensions are basically a nested for loop
sum([one * two for one in x for two in p_x])

#However, you could use zip() to turn the separate lists into a list of tuples:
sum([one * two for one, two in zip(x, p_x)])


#%%
"""REDUCE"""
#Reduce has been moved to the "functools" library, but understanding it will
#help your R coding.  Reduce applies a binary function to the first two 
#elements in a list, and keeps going until there's only one item left
from functools import reduce
alist = [55,21,12,100,15,88,71]

#The most common "reduce" is sum!
reduce(lambda x, y: x + y, alist)

#Find the highest odd number in a list
reduce(lambda x, y: y if y % 2 == 1 and y > x else x, alist, 0)


#%%
"""LIST COMPREHENSIONS"""
#List comprehensions have been widely embraced by the Python community.
#They are basically a way to do a for loop in a nice, convenient syntax

words = ["how","now","brown","cow"]
more_words = ["where","stare","fair","chair"]
#Get only the first letter of each word in the list
[word[0] for word in words]

#Return all words that are longer than 4 letters
[word for word in words if len(word) > 4]

#Notice how this returns the Cartesian product of the two lists:
[word1 + " " + word2 for word1 in words for word2 in more_words]

#This is because the above comprehension is essentially equivalent to the following:
for word1 in words:
    for word2 in more_words:
        word1 + " " + word2
        
#If a Cartesian product isn't what you wanted, remember that you can zip two or more lists together:
[word1 + " " + word2 for word1, word2 in zip(words, more_words)]

#You can also use a dictionary comprehension, but make sure the keys you're creating are unique!
unique_ids = [100,101,102,103]
names = ["Billy","Bobby","Bally","Sally"]
{key:value for key in unique_ids for value in names} #What happened?

#Here we go
{key:value for key, value in zip(unique_ids,names)}

#Finally, if you are dealing with really large datasets where you don't want to have the entire
#object in memory at once, you can use a generator comprehension instead:
(word1 + " " + word2 for word1, word2 in zip(words, more_words))

#Just like the iterables above, these generators must be iterated through using a for loop, or
#explicitly converted into a list using list()

#How would you find all the Pythagorean triples (a**2 + b**2 = c**2) using only the numbers 1-25?
[(a,b,c) for a in range(1,26) for b in range(1,26) for c in range(1,26) if a**2 + b**2 == c**2 and a <= b]

#%%
"""QUICKSORT"""
#Here is quicksort implemented in a procedural style:
def procsort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
                
        return procsort(less)+equal+procsort(greater)
    else:  
        return array
        
#Here it is written in a functional style:
def funcsort(arr): 
     if len(arr) <= 1:
          return arr
     else:
          return funcsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + funcsort([x for x in arr[1:] if x>=arr[0]])
          
          
alist = [15,22,7,88,23,41,1,2,1,9,2322]

print(procsort(alist))
print(funcsort(alist))