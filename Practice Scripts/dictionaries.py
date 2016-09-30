"""DICTIONARIES"""
#Dictionaries are an extremely useful collection for storing key-value pairs
#To create a dictionary:
mydict = dict()
print("Type of 'mydict = dict()' is {}".format(type(mydict)))

mydict = {}
print("Type of 'mydict = {{}}' is {}".format(type(mydict)))

#%%

#Dictionaries can contain anything!
mydict = {"bananas":2,"APPLES":"SEVEN!","Green??":True,"Concerns":None,"FavNums":[7,11]} 

#Get all the keys with .keys()
print(mydict.keys())

#Get all the values with .values()
print(mydict.values())

#And get the pairs with .items()
print(mydict.items())

#%%

mydict = {"bananas":2,"APPLES":"SEVEN!","Green??":True,"Concerns":None,"FavNums":[7,11]}
 
#Use "in" to search if a key exists in a dictionary
if "bananas" in mydict:
    print("B a n a n a s!")
    
#You can slice the dictionary to return only one value
print(mydict["APPLES"])

#Only use slicing if you *know* the value exists, because if it doesn't you will
#get an error and your program will crash if it isn't handled

#If you aren't sure if a key exists, use .get()
print(mydict.get("APPLES"))
print(mydict.get("apples?"))

#%%

mydict = {"bananas":2,"APPLES":"SEVEN!","Green??":True,"Concerns":None,"FavNums":[7,11]} 

#To add something to the dictionary, just assign to a key that isn't already used:
mydict["Aneesh"] = "Wow!"

print(mydict)

#To change something in the dictionary, just reassign the new value to the same key:
mydict["Green??"] = False

print(mydict)

#To delete something in the dictionary, use .pop("key")
mydict.pop("FavNums")
print(mydict)

#%%
"""DICTIONARY EXERCISES"""
#Remember the JSON example from Wikipedia?

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

#Try to assign this JSON to a dictionary.  It won't work.  Can you figure out why?
#Hint: JSON stands for JavaScript Object Notation, so the syntax is from JavaScript!

#Once you have it in proper Python syntax, do the following:
#John Smith just had his birthday today; please update his age accordingly


#John has just canceled his wireless plan.  Please delete the entry for his mobile number.
#Reminder:  Use .pop(keyname) to delete an item from a dictionary.


#Give John two children, Amos and Andy.


#Without retyping Amos and Andy, give John another child named Johnny Jr.


#Add a new key to John's record called "PersonID" and give it the value of 100.


#Change John's spouse value to 101.  This represents his spouse's PersonID.


#Create a dictionary for John's spouse, Jane.  Feel free to change her information if you want,
#except that her PersonID is 101, and her spouse's PersonID is 100.  Since most of Jane's
#information is the same, you can use the .copy() function to make a copy of John's record,
#instead of typing it all again from scratch.


#Finally create a new dictionary named PersonDB, and pass to it both John and Jane's
#dictionaries as values, with the keys being their respective PersonIDs.  Congratulations!
#You have just created a document database, one of the leading types of NoSQL databases.

