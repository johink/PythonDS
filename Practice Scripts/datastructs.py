#DATA STRUCTURES

#Lists are used to store values in a specific order

#Variables must always be assigned some value before they can be accessed
li = [] #Create an empty list

#append can be used to add values to the end of the list
li.append("Hello") #li == ["Hello"]
li.append("Goodbye") #li == ["Hello","Goodbye"]

#pop returns the last value in the list and removes it from the list
print("Popping: ",li.pop(),".. List now contains: ",li)

li = [0,1,3.14,10]

#Lists can be sliced the same way as strings
print(li[-1])
print(li[1:3])

#Advanced slicing... [startindex:endindex:step]
li = list(range(0,10))

print(li[::2]) #print every second value in the list
print(li[::-1]) #print the list in reverse
print(li[1:-1:2]) #subset the list to [1,2,3,4,5,6,7,8] and print every second item

#del deletes an arbitrary element in the list by index
del(li[5]) #li == [0,1,2,3,4,6,7,8,9]
del(li[5]) #now li == [0,1,2,3,4,7,8,9]

