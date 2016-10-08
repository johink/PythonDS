

""" Q1.
The school made a mistake in the undergraduate course catalog creating the 
identifiers and needs to find out which entries are messed up.  

The standard format for undergrad course identifiers is:  
-3 or 4 capital letter identifier for the Major, 
-a space, 
-then a 3 digit number (100-400) (note that these are exclusive boundaries), 
-and finally a possible extra letter from {G, L, S, H} to for special courses.

To find out which courses need to be updated, write a regular expression 
that matches only the proper format for a course identifier, then run it on 
each entry the course list and return a list where they do not match.

**Bonus**
Write the negation of the previous regex, one which only matches IMPROPER 
formatted identifiers.  Assume that improperly identified terms are:  
-3 or 4 capital letters,
-a space,
-any 3 digit number,
-any capital letter
"""


#TO-DO:  selection of good and bad course names from the catalog
course_list = []

#TO-DO:  assert statement that contains the bad entries from course_list
