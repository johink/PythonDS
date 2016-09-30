""" INTRO TO PYTHON SYNTAX by John Bourassa """
"""BASIC MATH"""
5 + 5
2 - 2
5 * 2 + 2 * 9
(2 + 7) * 3
5 / 2
5 // 2 #Floor division throws away the remainder
2 ** 3 #Exponentiation is **, not ^
2 ^ 3 #I told you this wouldn't work!


"""BOOLEAN VALUES"""
True #Note the capital T
False #This is case sensitive!

#Python uses words instead of symbols
not True
True and False
True and not False

#By default, Python evaluates not, then and, then or
False and False or True or False and True 
False and (False or True) or False and True #But parentheses work here as well

#You can also use integers with boolean operators
5 or 0
5 and 0


"""COMPARISON OPERATORS"""
1 == 1
0 == False
3 != 3
5 != [5] #Atomic value is different than list of 1 element
5 > 6
5 <= 9
7 < 8 < 9 #You can chain these in Python!
7 < 9 < 8


"""STRINGS"""
#A string consists of one or more characters surrounded by " or '
"This is a string"
"This is " + "a string" # addition concatenates strings
"This is " * 2 + "a string" # multiplication duplicates strings

"string"[0] #You can slice strings, along with many other things.  

"""IMPORTANT NOTE:
                   Python indices start at ZERO (not one)!
"""

len("string") #len can find the length of many things, including strings

#To use something that's not a string as a string, use str()
str(True)
str(3.14159)
"That's " + str(None) + " of your business!"

#Whether you use " or ' determines if you need to escape or not
#Printing quotes (") when the string is denoted by quotes (") requires escaping (\)
print('"No, I will not do that," Jake countered.')
print("\"No, I will not do that,\" Jake countered.")

#Printing an apostrophe (') when the string is denoted by quotes (") is perfectly fine
print("This just won't do...")
print('This just won\'t do...')


"""NONE"""
#None is kind of like NULL in a database
#Use the "is" operator to compare None, as well as other objects
5 is None
None is None


"""TRUTHY/FALSEY"""
#Python uses the concept of "truthiness" which exists in many programming languages
#Everything that is empty or zero is considered "falsey"
alist = ["hello",0,5.2,{},False,True,"",None,[]] #Which are truthy?
[x for x in alist if x] #Only truthy values remain


"""ASSIGNING VARIABLES"""

#Use =, <- does not work in Python
#Python's accepted syntax is to use words separated by underscores (_)
#Beware, you cannot put periods in variable names like with R
some_num = 1
some_num += 2 #These are shortcut operators, instead of "some_num = some_num + 2" 
# also try -= *= /= //= and **=

#Variables must be defined in some way before accessing their value
# is_not_defined * 2 #This will throw an error

#Remember that you can always find the type of a variable or literal with type()
type("Hello")
type(True)
type(None)
type(some_num)


"""BASIC DATA STRUCTURES"""
"""LISTS"""
#Lists are a relation of one or more elements.  They are always kept in the order you give them
courses = ["Data Visualization","Analytics Practicum","Data Management","Predictive Modeling","Analytics in the Bedroom"]
digits_of_pi = [3,1,4,1,5,9]

#However, lists do not have to contain just one data type
fav_things = ["Lucky Number Sleven",7,11]

#You can slice lists and get their length just like with strings
len(courses)
fav_things[1:]

#You can also find out if something is in a list
3 in digits_of_pi


"""SETS"""
#Sets are like the mathematical sets:  Duplicate values are automatically discarded.
#Order is not kept, so sets cannot be indexed, but len() and in still work
set(digits_of_pi)

#Sets are nice because you can do math with them, and they are very efficient
#Ex. you ask five students which course is their favorite, and want to find out which courses nobody chose
responses = ["Data Visualization","Analytics Practicum","Data Visualization","Predictive Modeling","Data Visualization"]
unloved = set(courses) - set(responses)


"""TUPLES"""
#Tuples are like lists, but they are immutable (i.e. their contents cannot be changed)
#Tuples have convenient syntax for dealing with multiple values at once
#Create a tuple by assigning a comma-separated list to a single variable
mytuple = ("Donuts (1 doz.)",3,5)
mytuple

mytuple = "Donuts (1 doz.)",3,5 #Parentheses are optional
mytuple

#A tuple's individual parts can be assigned to a comma-separated list of variables
item,qty,unit_price = mytuple

#You will see a better way of formatting strings like this, but for now:  concatenate!
print(str(qty) + "x " + item + " @ $" + str(unit_price) + " per") 

#This gives rise to a convenient method for swapping two values:
qty,unit_price = unit_price,qty
print(str(qty) + "x " + item + " @ $" + str(unit_price) + " per")


"""DICTIONARIES"""
#Dictionaries consist of key:value pairs.
#Keys can be any atomic data type, but they are generally strings
#Values can be literally anything, including other dictionaries!
John = {"nickname":"Johnny B","age":12,"cool?":False,"likes":["Trampoline Park","Python","Ping Pong"]}
John["nickname"]
John["likes"]
John["likes"][1]

Chase = {'nickname':'High-Speed','age':14,'cool?':True,'likes':['Ping Pong','SAS','Trampoline Park']}
Martha = {"nickname":"Top Dawson",'age':17,"cool?":True,"likes":["R",'Duke Energy',"Probably Cats?"]}

students = [John,Chase,Martha] #Note how the order of the keys has been changed

[student for student in students if student["cool?"]]
[student["age"] for student in students if "Ping Pong" in student["likes"]]


#Dictionaries are very powerful, and are quite similar to JSON which is a very common data-exchange format
#Example JSON:

""" JSON example from Wikipedia
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 25,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    },
    {
      "type": "mobile",
      "number": "123 456-7890"
    }
  ],
  "children": [],
  "spouse": null
}
"""


"""BASIC CONTROL FLOW STATEMENTS"""
"""IF"""
#If works the same as R, but "else if" has been shortened to "elif"
#%%
drink_order = "Coke"
if drink_order == "water":
    print("This one's on the house, sweetheart!")
elif drink_order == "beer":
    print("I'm going to need to see some ID, mister.")
else:
    print("We don't have any " + drink_order + ".")
#%%
#Multiple commands can be placed inside of an if/elif/else block by just keeping the same indentation
excited_for_school = True
python_points = 0
#%%
if excited_for_school:
    print("You feel inspired to go to school; you gain five Python points!")
    python_points += 5
    print("...all that learning made you tired...")
    excited_for_school = False
else:
    print("You feel drained, so you watch some Netflix and take a nap.")
    print("What a great rest!  You feel ready to learn everything now.")
    excited_for_school = True
print("Current Python points: " + str(python_points))
#%%
#In addition to controlling program flow, if can also be used in an expression:
num_pizzas = 8
enough_pizza = "Yes" if num_pizzas >= 10 else "No"
enough_pizza

#This is really just a nicer way of writing the following:
if num_pizzas >= 10:
    enough_pizza = "Yes"
else:
    enough_pizza = "No"
enough_pizza
#%%


"""WHILE"""
#While loops repeatedly run until their condition is no longer True
i = 0
while i < 5:
    print(i)
    i += 1
#%%
#Care is required with while loops, because if they are improperly specified, they can run forever
#For example, if we forgot to add one to i in the previous loop, it would forever print the value 0
""" Only run if you like infinite loops!
i = 0
while i < 5:
    print(i)
"""
#%%
#While loops are useful when the number of iterations is not well-defined
#Here we will roll a die until we get a 6
import random
dieroll = 0
while dieroll != 6:
    dieroll = random.randint(1,6)
    print("You rolled a " + str(dieroll) + "!")
#%%    
    
    
"""FOR"""
#For loops can be used in two ways:  
#To iterate over a collection (e.g. list, tuple, dictionary, set)
John = {"nickname":"Johnny B","age":12,"cool?":False,"likes":["Trampoline Park","Python","Ping Pong"]}
Chase = {'nickname':'High-Speed','age':14,'cool?':True,'likes':['Ping Pong','SAS','Trampoline Park']}
Martha = {"nickname":"Top Dawson",'age':17,"cool?":True,"likes":["R",'Duke Energy',"Probably Cats?"]}
students = [John,Chase,Martha]

#Print likes for each student
for student in students:
    print(student["likes"])
    
#Find everything that is liked by at least one student
liked = set()
for does_not_matter in students:
    liked.update(does_not_matter["likes"])
print(liked)

#Find the average student age
total_age = 0
num_students = 0
for student in students:
    total_age += student["age"]
    num_students += 1
print("Average age is " + str(total_age/num_students))
#%%

#To iterate over a range of numbers
for i in range(5):
    print(i)
    
for does_not_matter in range(len(students)):
    print("The " + str(does_not_matter) + " element in the students collection has a nickname of " + students[does_not_matter]["nickname"])
#%%


"""FUNCTIONS"""
#Functions make your life easier (trust me!) 
#by preventing you from having to retype the same thing over and over again
def conf_int(data, clevel = .9):
    from scipy import stats
    import numpy as np
    from math import sqrt
    tstat = stats.t.ppf(clevel,len(data)-1)
    avg = np.mean(data)
    se = np.std(data)/sqrt(len(data))
    return (avg - se * tstat, avg + se * tstat)

#Let's use our conf_int function to run a hypothesis test!
hyp_mean = 12   
some_nums = [5,2,3,1,8,22,1,3,2,17]
lb,ub = conf_int(some_nums,.95)
print("Is {} in our interval of {} - {}?".format(hyp_mean,lb,ub))
if lb < hyp_mean < ub:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis")