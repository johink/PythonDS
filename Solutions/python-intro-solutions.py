""" INTRO TO PYTHON SYNTAX by John Bourassa """
"""BASIC MATH"""
5 + 5
2 - 2
5 * 2 + 2 * 9
(2 + 7) * 3
5 / 2
5 // 2 #Floor division throws away the remainder
5 % 2 #Modulo division keeps only the remainder
2 ** 3 #Exponentiation is **, not ^
2 ^ 3 #I told you this wouldn't work!

2.2 * 2 #Numbers with decimals are floating-point
15 * 1.0 #This is called "type coercion"  Even though 15 * 1.0 is clearly 15, the 15 was coerced into a float in order to be multiplied


"""BOOLEAN VALUES"""
True #Note the capital T
False #This is case sensitive!

#Python uses words instead of symbols
not True
True and False
True and not False

#By default, Python evaluates not, then and, then or
False and False or True 
False and (False or True) #But parentheses work here as well

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


"""CHANGING TYPES"""
int(3.5) #int throws away the remainder; use round instead if that's your goal
round(3.5)
str(True)
float("5.323")
float("$5.32") #Float doesn't understand how to read this, so it throws an error!
bool(1)
bool("False") #Is this what you expect?


"""NONE"""
#None is like NULL in a database
#Use the "is" operator to compare None, as well as other objects
5 is None
None is None


"""TRUTHY/FALSEY"""
#Python uses the concept of "truthiness" which exists in many programming languages
#Everything that is empty or zero is considered "falsey"
alist = ["hello",0,5.2,{},False,True,"",None,[]] #Which are truthy?
[x for x in alist if x] #Only truthy values remain

#If you forget whether something is falsey or not, just pass it to bool()
bool(None)
bool([None])


"""ASSIGNING VARIABLES"""

#Use =, <- does not work in Python
#Python's accepted syntax is to use words separated by underscores (_)
#Beware, you cannot put periods in variable names like with R
some_num = 1
some_num = some_num + 2
some_num += 2 #These are shortcut operators, instead of "some_num = some_num + 2" 
# also try -= *= /= //= and **=

#Variables must be defined in some way before accessing their value
is_not_defined * 2 #This will throw an error

#Remember that you can always find the type of a variable or literal with type()
type("Hello")
type(3.14)
type(True)
type(None)
type(some_num)



"""CHECKPOINT"""
#Each U.S. state has 2 Senators; how many senators are there in total?  Store the result in a variable named num_senators
num_senators = 2 * 50

#There is currently 1 House Representative for every 733,103 people in the U.S.  
#If the current U.S. population is 318,900,000, how many Representatives are there?
#Put your answer in a variable called num_representatives
num_representatives = round(318900000 / 733103)

#During the U.S. election, the winning candidate must receive a majority (greater than 50%) of electoral votes.  
#The number of electoral votes is equal to the number of senators plus the number of representatives.
#How many votes must a candidate receive at a minimum to win the election?
min_votes = (num_senators + num_representatives) // 2 + 1

#As Albert Einstein once famously said, "E = mc^2"
#People think this has to do with relativity theory, but you know better, as the formula clearly means:
#Enjoyment = milk * cookies^2
#You like to drink a glass of milk after every five cookies
#If you're planning on eating 13 cookies, how much Enjoyment are you about to receive?
Enjoyment = (13 // 5) * 13 ** 2



"""BASIC DATA STRUCTURES"""
"""LISTS"""
#Lists are a collection of one or more elements.  The elements are always kept in the order you give them
courses = ["Data Visualization","Analytics Practicum","Data Management","Predictive Modeling","Analytics in the Bedroom"]
digits_of_pi = [3,1,4,1,5,9]

#However, lists do not have to be homogeneous
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
responses = ["Data Visualization","Analytics Practicum","Data Visualization","Data Management","Data Visualization"]
unloved = set(courses) - set(responses)


"""TUPLES"""
#Tuples are like lists, but they are immutable (i.e. their contents cannot be changed)
#Strings are another immutable data type.  Basically, if you alter a string or a tuple, it creates a new one!
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

#You can access a key's associated value by passing in the key
John["nickname"]
John["likes"]

#If the value you get back can also be further subsetted, feel free to keep going!
John["likes"][1]

Chase = {'nickname':'High-Speed','age':14,'cool?':True,'likes':['Ping Pong','SAS','Trampoline Park']}
Martha = {"nickname":"Top Dawson",'age':17,"cool?":True,"likes":["R",'Duke Energy',"Probably Cats?"]}

#Now we have a list of dictionaries
students = [John,Chase,Martha] #Note how the order of the keys has been changed

#These are list comprehensions to show you how easy it is to slice lists & dictionaries
#We will cover list comprehensions in the "Advanced Python Programming" section
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


"""CHECKPOINT"""
#Create a shopping list for your next trip to the grocery store.  Check if ice cream is in your list.
shopping_list = ["Cookies","Cake","Cupcakes","Ice Cream"]
"Ice Cream" in shopping_list

#Create a "you" dictionary.  Add at least 4 keys, and make at least one of the values non-atomic (aka another data structure)
{"name":"John","age":23,"numbers":[3,5,2],"grade":12}

#Create a list containing each individual digit of your phone number.
phone_no = [1,5,3,2,5,2,3,3,2,1]

#Turn that list into a set.  What's the length of your set?  If it's 10, you have a very lucky phone number!
len(set(phone_no))

#Create a "you"ple using the same information as your "you" dictionary.  Which of these makes more sense to use, and why?
("John",23,[3,5,2],12)

#%%
"""CONTROL FLOW STATEMENTS"""
"""IF"""

#If works the same as R, but "else if" has been shortened to "elif"
drink_order = "Chase"
if drink_order == "water":
    print("This one's on the house, sweetheart!")
elif drink_order == "beer":
    print("I'm going to need to see some ID, mister.")
else:
    print("We don't have any " + drink_order + ".")
    
#%%
excited_for_school = True
python_points = 0

#%%

#Multiple commands can be placed inside of an if/elif/else block by just keeping the same indentation
if excited_for_school:
    print("You feel inspired to go to school; you gain five Python points!")
    python_points += 5
    print("...all that learning made you tired...")
    excited_for_school = False
else:
    print("You feel drained, so you watch some Netflix and take a nap.")


    #The extra space doesn't mean anything.  As long as the indentation is the same,
    #the statements below belong to the else: statement
    print("What a great rest!  You feel ready to learn everything now.")
    excited_for_school = True
    
#Note how this print function always runs because it's not indented like the rest
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
#While loops are useful when the number of iterations is not well-defined (also known as non-deterministic)
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

#%%
#Print likes for each student
for student in students:
    print(student["likes"])
   
#%%   
#Find everything that is liked by at least one student
liked = set()
for does_not_matter in students:
    liked.update(does_not_matter["likes"])
print(liked)

#%%
#Find the average student age
total_age = 0
num_students = 0
for student in students:
    total_age += student["age"]
    num_students += 1
print("Average age is " + str(round(total_age/num_students,2)))
#%%

#To iterate over a range of numbers
for i in range(5):
    print(i)

#%%
for does_not_matter in range(len(students)):
    print("The " + str(does_not_matter) + " element in the students collection has a nickname of " + students[does_not_matter]["nickname"])

#%%


"""CHECKPOINT"""
#Check again if there's ice cream in your shopping list.  If there is, print "Yay!" and if not, print "Aww :("
if "Ice Cream" in shopping_list:
    print("Yay!")
else:
    print("Aww :(")
             
#%%                                                                                                
#Create a for loop which adds all the odd numbers between 1 and 20
#Remember that range(x,y) gives numbers starting from x up to but not including y
result = 0
for i in range(1,21):
    if i % 2 == 1:
        result += i
print(result)

#%%
#Do the same thing as the for loop above using a while loop instead.  Why is this a dumb idea? 
result = 0
while i <= 20:
    if i % 2 == 1:
        result += i
    i += 1
print(result)


#%%
"""FUNCTIONS"""
#Functions make your life easier (trust me!) 
#by preventing you from having to retype the same thing over and over again
#Think back to databases:  Why do we only want to store a value once?  Writing a function is similar.
#Just like fors and ifs, all of the indented code below the def xxx: statement belongs to the function
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
#%%
    
"""CHECKPOINT"""
#Write a function which takes in a shopping list, checks if ice cream is on the list and prints "Yay!" if it is or "Aww :(" if it isn't
def check_list(mylist):
    if "Ice Cream" in mylist:
        print("Yay!")
   
check_list(shopping_list)                  
#%%                                                                                                     
#Write a function which returns the number of unique items in its input list
def num_unique(mylist):
    return len(set(mylist))

num_unique(phone_no)    
#%%
#Write a function which adds all the numbers in the input list and returns the sum (without using the sum function)
def mysum(mylist):
    result = 0
    for item in mylist:
        result += item
    return result

mysum(phone_no)