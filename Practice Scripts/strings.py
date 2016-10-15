"""STRINGS"""

#Strings are immutable (i.e. they cannot be modified after creation)

#Both " and ' work to denote strings
onestring = 'string'
twostring = "string"

type(onestring) == type(twostring)

#%%
#Triple " and ' allow multiline strings
multiline = """This just happens to be a striiiiiiii
iiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnnnnn
nnnnnnnnnnggggggggggggggggg"""
print(multiline)

#%%
#\n is newline
#\t is tab
print("First Line\nSecond\t\tLine")

#%%
#Whether you use " or ' determines if you need to escape or not
#Printing quotes (") when the string is denoted by quotes (") requires escaping (\)
print('"No, I will not do that," Jake countered.')
print("\"No, I will not do that,\" Jake countered.")

#Printing an apostrophe (') when the string is denoted by quotes (") is perfectly fine
print("This just won't do...")
print('This just won\'t do...')

#%%
#+ is concatenation
"Box" + "Car"

#* is repetition
"Box"*4

#%%
#Must use str() to treat non-strings as strings
demand = 1
#request = "Hello, I would like " + demand + " cookies"  <-- Error
request = "Hello, I would like " + str(demand) + " cookies"

#%%
#Can index individual characters in a string
print("Hello"[0])

#Can index with negative numbers
print("Hello"[-1]) #Last character

# o  l  l  e  H  e  l  l  o
#-4 -3 -2 -1  0  1  2  3  4 

#%%
#Raw strings ignore escape characters (i.e. '\'), this is very useful for Regular Expressions
r"Open up C:\Python\fun.py" == "Open up C:\\Python\\fun.py"

#%%
#Slicing strings with [:]
print("Hello"[1:3]) #Read as "From character 1, up to but not including character 3"

#Negative indexes work as well
print("Hello"[1:-1]) #From character 1, up to but not including the last character

#Omitting an index indicates start at beginning / continue to end
print("Hello"[:3])
print("Hello"[4:])

#%%
#Giving an out-of-bounds index will still work
"Hello"[1:25000]

#%%
#This makes it very simple to split a string into two parts:
greeting = "Hello"
aliengreeting = greeting[2:] + greeting[:2]
print(aliengreeting)

#%%
"""USEFUL STRING FUNCTIONS:

lower(), upper()
strip("chars") <-- trim leading/trailing instances of all characters in "chars".  strip() strips only whitespace
isalpha(), isdigit(), isalnum(), isspace() <-- all chars are of specified type
startswith("other"), endswith("other")
find("other") <-- returns index of first occurrence or -1 if not found
replace("old","new")
split("delim") <-- split() splits on whitespace
join(list) <-- called-upon string used to delimit list
format(args) <-- Fill in {}s with args

"""

#%%
example = "Alfred R. Penningtonsmith"

print(example.lower())
print("Hello".upper())

#%%

print("    W hy not  ? ".strip())
print("    W hy not  ? ".strip(" ?"))

#%%
#These iswhatever() functions can be used for input validation
"123".isdigit()
"12ab3".isalpha()
"12ab3".isalnum()
"\t  \n".isspace()

#%%
example = "Alfred R. Penningtonsmith"

print(example.startswith("smith"))
print(example.endswith("smith"))

#%%
print(example.find("fred"))
print(example.find("Fred"))

#%%
print(example.replace("n","m"))

#%%
print(example.split())
print(example.split(".")) #Whitespace is kept!  Now we are just splitting on '.'

#%%
words = ["One","Two","Red","Blue","!"]
print(" ".join(words))
print(" Fish ".join(words))

#%%
import random
words1 = ["Sir","Ma'am","Son","Panda","Kitty"]
words2 = ["day","life","meal","trip","rest","trip to the Moon","flight"]

"Goodbye {}, have a nice {}!".format(words1[random.randrange(len(words1))], words2[random.randrange(len(words2))])

#%%
orderitems = [("Toothpaste",3,2.49),("Toothbrush",1,4.00),("Floss",2,1.20)]

for item in orderitems:
    print("{}x {:<12} @ ${:0<4.2} per = ${:0<4.2}".format(item[1], item[0], item[2], item[1]*item[2]))

#%%

"""STRING EXERCISES"""
#Use find to print out just the TLD (Top-Level Domain, e.g. 'com') for each email in this list of email addresses
#You can assume that all TLDs are just three letters
#For bonus points, do it in a for loop and only write the code once!
emails = ["jb123@au.edu Johnny B", "ShootToBill@aol.com Bill Turner","xX_TigerKittyMeow_Xx@aspca.org Veronica Katz","FlawedRibbon@msn.com Ricky Sticky"]

#%%
#Use string slicing and repetition to turn "Missing Pie" into "Mississippi"
startword = "Missing Pie"
finishword = "Replace me with string functions!"
finishword == "Mississippi"

#%%
#Define a function which will take in a string and return a "crazy" string by randomly capitalizing letters and inserting a random amount of space between words
#Example Input:  "Hello!"
#Example Output: "hELlo!"
#Hint random.random() gives you the same thing as the Excel rand() function!


#Using your crazy string function, convert this seemingly innocuous sentence into a ransom letter and send it to your friend:
letter = "Have you seen your cat recently?  I wonder where it could have run off to!  I'm sure it will turn up... somewhere."

