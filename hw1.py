"""HOMEWORK ONE"""

""" Q1.
Since you have been looking for jobs lately, you've decided to write a function
which will automatically tell you if you are qualified for a job posting or not

Being qualified for a job posting means that you have all of the skills listed
in the requirements

The function will take in a list of jobs, and a list of your skills, and return
both the name of the company and the position for which you are qualified for
"""
#%%

my_skills = ["Excel","SQL","R","Python","Visualization","Modeling","Statistics"]

jobs = [{"Company":"Google",
         "Position":"Data Scientist",
         "Location":"San Francisco, CA",
         "Requires":["Python","Visualization","Hadoop","SQL"]},
        {"Company":"Uber",
         "Position":"Business Analyst",
         "Location":"San Francisco, CA",
         "Requires":["Excel","SQL","R","Modeling"]},
        {"Company":"Ricky's Pawn & Auto",
         "Position":"Chief Information Officer",
         "Location":"Winston-Salem, NC",
         "Requires":["Excel","Street Smarts"]}]

def qualified(jobs, skills):
    results = [] #Add the jobs you qualify for to results as a tuple (company, position)
    return results

assert qualified(jobs, my_skills) == [("Uber","Business Analyst")]

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
  
#%%
         
""" Q3.
In the hit game Dungeons & Dragons, players roll many abnormally-sided dice.  One of
these dice is a 20-sided die, also referred to as a "d20."  In the game, rolling a 20
is usually considered an "automatic success" or "critical success."

Using random number generation and control structures, create a distribution of the number
of d20 rolls it takes to score a critical success for 10,000 trials.  In other words, at
each trial, keep rolling the die until it comes up 20, and keep track of the number of rolls.
Repeat this until you have gotten 10,000 successes.  It's up to you to decide which data
structure would be best for storing this information!
"""
import random
print(random.randint(1,20)) #Here is your d20!