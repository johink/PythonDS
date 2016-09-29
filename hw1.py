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

def qualified(jobs, skills):
    return

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
         
print(qualified(jobs, my_skills))

#%%

""" Q2.

"""