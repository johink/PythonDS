"""LISTS"""
#Lists are used to store values in a specific order

#Variables must always be assigned some value before they can be accessed
li = [] #Create an empty list
li = list() #Same thing

#append can be used to add values to the end of the list
li.append("Hello") #li == ["Hello"]
li.append("Goodbye") #li == ["Hello","Goodbye"]
li.append("Little")
li.append("Guy")
print("List contains: {}".format(li))
#pop returns the last value in the list and removes it from the list
print("Popping: ",li.pop(),".. List now contains: ",li)

#pop can also pop at a specified index
print("Popping: ",li.pop(0),".. List now contains: ",li)


#%%
li = [0,1,3.14,10]

#Lists can be sliced the same way as strings
print(li[-1])
print(li[1:3])

#%%
#Lists can be added to one another
list1 = list(range(5))
list2 = list(range(5,10))
list2 + list1

#However, do not use += if you are storing the combined list, as it is extremely inefficient
#Use .extend() instead
list1.extend(list2)
list1

#%%
#Advanced slicing... [startindex:endindex:step]
li = list(range(10))

print(li[::2]) #print every second value in the list
print(li[::-1]) #print the list in reverse
print(li[1:-1:2]) #subset the list to [1,2,3,4,5,6,7,8] and print every second item

#%%
li = list(range(10))
#del deletes an arbitrary element in the list by index
del(li[5]) #li == [0,1,2,3,4,6,7,8,9]
print(li)

del(li[5]) #now li == [0,1,2,3,4,7,8,9]
print(li)

#%%
li = ["tomatoes","onions","sausage","cheese","sausage"]
#remove() deletes the first instance of the argument you specify
li.remove("onions")
li

li.remove("sausage")
li

#%%
li = ["tomatoes","onions","sausage","cheese","sausage"]
#Similarly, index() gives you the index of the argument you specify
print(li.index("onions"))
print(li.index("sausage"))

#%%
#Many list actions can result in errors.  This is why input validation is so important
li = list(range(5))

li[5]
del(li[5])
li.pop(5)
li.remove(5)
li.index(5)

print("Running life-or-death code here!") #Note how this code never runs because an unhandled error occurs

#%%
"""SORTING LISTS"""
#Lists of information are often needed to be put in some meaningful order
#The sorted() function will accomplish this for you!
li = [5,1,9,22,1,3,2,33]

#Default sort 
print(sorted(li))
print(sorted(li, reverse = True))

#The underlying list is not changed
print(li)

#%%
li = ["How","now","brown","cow"]

print(sorted(li)) #The capital H throws off the ordering!

#You can also specify a custom "key" to sort by, if the default one doesn't accomplish your goals
#Here our key will compare the words in lower case, so they will be in the proper order
print(sorted(li,key = str.lower))

print(sorted(li, key = len))

#Any function that takes in an atomic value and returns an atomic value can be used as a key
#Including user-defined functions
def get_key(x):
    return x[1::-1]
print(sorted(li, key = get_key)) #Can you tell what the function is returning?

#%%

"""LIST EXERCISES"""
#%%
#Given a list of strings, return the number of strings containing the word "cart" and ending with the letter "r"
def cart_r(x):
    #Your code here
    return 

a_list_of_strings = ["carter","cartridge","carthage","welcome back carter","fly carter airliner"]
assert cart_r(a_list_of_strings) == 3

a_list_of_strings = ["carrtrr","carts are smart","a cart apart","kickcart my heart"]
assert cart_r(a_list_of_strings) == 0

print("If this prints, you were successful!")

#%%
#Given a list of tuples containing line items for a receipt, sort the tuples by
#Total price paid for that item

def total_price(x):
    #Your code here
    return

line_items = [("Cake",1,21.99),("Streamers",10,1.99),("Plasticware",2,3.99),("Confetti Gun",1,1500.00),("Sad Clown",8,100.00)]

print(sorted(line_items, key = total_price))

#%%
#Given a list, return a list where all the consecutive duplicates have been removed
def remove_dups(x):
    #Your code here
    return

li = [1,2,3,3,3,1,2,1,1,999999]
assert remove_dups(li) == [1,2,3,1,2,1,999999]

li = ["red","orange","yellow","green","blue","indigo","violet"]
assert remove_dups(li) == ["red","orange","yellow","green","blue","indigo","violet"]

print("If this prints, you were successful!")