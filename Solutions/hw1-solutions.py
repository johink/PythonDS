"""HOMEWORK ONE"""

""" Q1.
Since you have been looking for jobs lately, you've decided to write a function
which will automatically tell you if you are qualified for a job posting or not

Being qualified for a job posting means that you have all of the skills listed
in the requirements

The function will take in a list of jobs, and a list of your skills, and return
both the names of the companies and the positions for which you are qualified
"""
#%%

my_skills = ["Excel","SQL","R","SAS","Python","Visualization","Modeling","Statistics"]

jobs = [{"Company":"Stewgle",
         "Position":"Data Scientist",
         "Location":"San Francisco, CA",
         "Requires":["Python","Visualization","Hadoop","SQL"]},
        {"Company":"Super",
         "Position":"Business Analyst",
         "Location":"San Francisco, CA",
         "Requires":["Excel","SQL","R","Modeling"]},
        {"Company":"Ricky's Pawn & Auto",
         "Position":"Chief Information Officer",
         "Location":"Winston-Salem, NC",
         "Requires":["Excel","Street Smarts"]},
        {"Company":"KRAS",
         "Position":"Consultant",
         "Location":"Raleigh, NC",
         "Requires":["SAS","Excel","SQL","Modeling","Statistics"]}]

def qualified(jobs, skills):
    #Let's use pseudo-code to break this problem down:
    #First, we'll create a list to hold our results
    results = []
    
    #Now, we'll look at each job posting:
    for job in jobs:
        #Check if we qualify for the current job posting:
        #Remember that you can check if a set is a super-set or sub-set of another set by using >= and <=
        #Additionally, you could also use the "in" operator to see if all the required skills are in your list of skills
        #This is the subset operator.  It returns true when the thing on the right has all the elements of the thing on the left.
        if set(job["Requires"]) <= set(skills):
            #If we do qualify, add (Company, Position) to results:
            results.append((job["Company"],job["Position"]))


    return results

assert qualified(jobs, my_skills) == [("Super","Business Analyst"),("KRAS","Consultant")]

print("If you get here, you did it!")

#%%

""" Q2.
Using the exercise data below, find out how much total weight has been lifted by
each muscle group using a for loop.  Keep the running totals in a dictionary where
the keys correspond to the different muscle groups.
"""

workout = [("chest",("Incline Bench",8,135)),("triceps",("Skull-Crushers",12,35)),
           ("chest",("Incline Bench",6,225)),("triceps",("Skull-Crushers",6,55)),
           ("shoulders",("Shoulder Press",8,30)),("chest",("Dumbbell Flys",12,15)),
           ("shoulders",("Shoulder Press",5,60)),("chest",("Dumbbell Flys",16,25)),
           ("triceps",("Dips",8,45)),("triceps",("Triceps Extension",8,35)),
           ("triceps",("Dips",14,45)),("triceps",("Triceps Extension",6,75)),
           ("chest",("Bench Press",6,315)),("chest",("Dumbbell Flys",7,35)),
           ("chest",("Bench Press",1,405)),("chest",("Dumbbell Flys",2,85))]

results = {}
for exercise in workout:
  #results.get(key, default) returns the value associated with key, or default if the key is not in the dictionary
  #If the nested nature of the "workout" variable is confusing, try playing with it in the IPython console at the bottom right
  #by arbitrarily slicing it until you better understand its structure.
  #For example, workout[0], workout[0][0], workout[0][1][0], etc.
  results[exercise[0]] = results.get(exercise[0], 0) + exercise[1][1] * exercise [1][2]


assert results == {'chest': 5720, 'triceps': 2470, 'shoulders': 540}

print("If you get here, you did it!")
           
#%%

""" Q3.
In the hit game Dungeons & Dragons, players roll many abnormally-sided dice.  One of
these dice is a 20-sided die, also referred to as a "d20."  In the game, rolling a 20
is usually considered an "automatic success" or "critical success."

Using random number generation and control structures, create a distribution of the number
of d20 rolls it takes to score a critical success for 10,000 trials.  In other words, at
each trial, keep rolling the die until it comes up 20, and keep track of the number of rolls.
Repeat this until you have gotten 10,000 successes.  You should use a list to keep track of these
rolls, which we will use to graph the distribution!
"""
import random
print(random.randint(1,20)) #Here is your d20!
my_data = []

#We need to loop 10,000 times
for i in range(0,10000):
  #At each loop, roll the die repeatedly until you get a 20, and keep track of the number of rolls
  dieroll = 0
  num_rolls = 0
  while dieroll != 20:
    dieroll = random.randint(1,20)
    num_rolls += 1
    
  #Add the number of rolls to the my_data list
  my_data.append(num_rolls)

#%%
#After you have your 10,000 numbers, run this code to see the distribution:
import pandas as pd
vector_of_rolls = pd.Series(my_data)
vector_of_rolls.plot.hist()
vector_of_rolls.mean()
