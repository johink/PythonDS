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
mydf[mydf["age"] >= 13]
    
    
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



"""REDUCE"""



"""LIST COMPREHENSIONS"""


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