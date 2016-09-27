"""SETS"""
#Sets are like mathematical sets.  They automatically remove duplicates and are very efficient.
#To create an empty set:

myset = set()
print("Type of 'myset = set()' is {}".format(type(myset)))

#This does not work!  {} creates an empty dictionary
myset = {}
print("Type of 'myset = {{}}' is {}".format(type(myset)))

#%%

setA = set([1,3,5,2,2,2,1,9])
setB = {1,3,3,3,5,7,9}

print("Set A = {}".format(setA))
print("Set B = {}".format(setB))

#Set intersection (i.e. items in both A and B)
print("A and B = {}".format(setA & setB))

#Set union (i.e. items in either A or B)
print("A or B = {}".format(setA | setB))

#Set difference (i.e. items in A that are not in B)
print("A minus B = {}".format(setA - setB))

#Set symmetric difference (i.e. items that are in either A, or B, but not both)
print("A ^ B = {}".format(setA ^ setB))

#%%

#Adding items to a set is easy!
myset = set()

myset.add(5)
myset.add(3)
myset.add(5)

print(myset)

#Sets aren't sorted, but we can fix that with the sorted() function!
print(sorted(myset))

#%%

#You can see if all elements of one set are contained in another set
setA = set([1,3,5])
setB = set([1,2,3,4,5])

#Is A a superset of B?  Does A contain all the elements in B?
print(setA >= setB)

#Is A a subset of B?  Does B contain all of the elements in A?
print(setA <= setB)

#%%

#Practical applications of sets:
#Say you are running a summer camp, and you have a dictionary containing
#all the children, along with the activities they have signed up for.
#You need to make sure that the activities which nobody has signed up for are canceled

activities = ["Dressage","Swimming","Baking","Candlestick Making","Hang Gliding","Boxing","Mixed Martial Arts","Quilting","Board Games"]

children = [{"name":"Billy","activities":["Swimming","Dressage","Board Games"]},
            {"name":"Bobby","activities":["Dressage","Baking","Swimming"]},
            {"name":"Babby","activities":["Swimming","Mixed Martial Arts","Board Games"]},
            {"name":"Bully","activities":["Boxing","Swimming","Board Games"]},
            {"name":"Bebby","activities":["Swimming","Hang Gliding","Dressage"]},
            {"name":"Bibby","activities":["Board Games","Dressage","Boxing"]}]
            
#%%            
#Which activities should be canceled?  Using sets makes this question a lot easier to answer!
#There are a couple ways it could be done...
#You could delete activities from the list as you see them:
unseen_activities = set(activities)

for i in range(len(children)):
    unseen_activities -= set(children[i]["activities"])
    print("Unseen activities after {} child: {}".format(i+1,unseen_activities))

#Now we should have the activities no one has signed up for:
print("We should get rid of: {}".format(unseen_activities))

#%%
#Or you could accumulate the activities as you go, and then subtract at the end
seen_it = list()

for child in children:
    seen_it.extend(child["activities"])

print("All activities: {}".format(seen_it))

print("We should get rid of: {}".format(set(activities) - set(seen_it)))

#%%
"""SET EXERCISES"""
#Your friend really likes to work out (he does a lot of sets), and was wondering if you could write him a function to help him
#make sure that he's doing enough exercises for each body part.  Luckily, he takes detailed notes of each workout he completes,
#and he has provided these to you.  Unfortunately, he records them in a "stream of consciousness" style, meaning that he records
#each exercise right as he does them.  An exercise looks like this:  (Exercise_name, reps, weight).  Since your friend knows
#you don't really care about working out, he has annotated which body part each exercise is for

workout = [("chest",("Incline Bench",8,135)),("triceps",("Skull-Crushers",12,35)),
           ("chest",("Incline Bench",6,215)),("triceps",("Skull-Crushers",6,55)),("shoulders")]

