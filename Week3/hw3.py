"""HOMEWORK THREE"""

""" Q1.
The school made a mistake in the undergraduate course catalog creating the 
identifiers and needs to find out which entries are messed up.  

The standard format for undergrad course identifiers is:  
-3 or 4 capital letter identifier for the Major, 
-a space, 
-then a 3 digit number (100-400, where 100,200,300,400 are excluded) , 
-and finally a possible extra letter from {G, L, S, H} to for special courses.

To find out which courses need to be updated, write a regular expression 
that matches only the proper format for a course identifier, then run it on 
each entry the course list and return a list where they do not match.

**Bonus**
Write the negation of the previous regex, one which only matches IMPROPERLY 
formatted identifiers.  Assume that improperly identified terms are:  
-3 or 4 capital letters,
-a space,
-any 3 digit number,
-any capital letter
"""

course_list = ['ART 156', 'ART149G', 'ART 196', 'ART 212L', 'ART 245', 'ART 227', 'ART 251', 'ART336', 'ARTTT 377', 'ART 381', 'BIO 134', 'BIO2 105', 'BIO 149S', 'BIO 223', 'BIO 244H', 'BIO 250', 'BIO 233T', 'BIO 384', 'BIO 364', 'BIO 305', 'CSC 126D', 'CSC 114', 'CSC 130E', 'CSC 285', 'CS 284G', 'CSC 236', 'CSC 265', 'CSCI 357', 'CSC 304S', 'CSC 388', 'GTCS 198H', 'GTCS 171', 'GTCS 004', 'GTCS 251S', 'GTCS 280', 'GTCS 285W', 'GTCS 218', 'GTCS 365', 'GTCS 488', 'GTCS 342P', 'LIN 173', 'LIN 024', 'LIN 150', 'LIN 290', 'LIN 234', 'LIN 248L', 'LIN 550', 'LIN 326', 'LIN 349', 'LIN 349L', 'MTH 169', 'MTH188', 'MTH 113', 'MTH 251H', 'MTH 248', 'MTH 200', 'MTH 232', 'MTH 365H', 'MTH 388', 'MTH 371', 'POL 170S', 'POL 102', 'POLs 104', 'POL 281', 'POL 240H', 'POL 285', 'PO 256', 'POL 326', 'POL 383', 'POL 369X', 'ROM 191', 'ROM 119Y', 'ROM 191', 'ROM 217', 'ROM 280HI', 'ROM 237', 'ROM 219S', 'ROM 350', 'ROM 314', 'ROM 318']

answer = []

assert answer.sort() ==  ['ART149G', 'ART336', 'ARTTT 377', 'BIO2 105', 'BIO 233T', 'CSC 126D', 'CSC 130E', 'CS 284G', 'GTCS 004', 'GTCS 285W', 'GTCS 488', 'GTCS 342P', 'LIN 024', 'LIN 550', 'MTH188', 'POLs 104', 'PO 256', 'POL 369X', 'ROM 119Y', 'ROM 280HI'].sort()

#%%

""" Q2.
Much to your chagrin, your organization likes to store all employee information in flat files.
For example, the employee record for Pippy Longstocking is as follows:
"""

# Longstocking, Pippy A. Accountant II $65,000 (123) 456-7890 palongs@abc.com 2007-03-21

"""
Unfortunately, it's time for the monthly update of employee information.
This process usually takes the secretary Bobby an entire day to complete,
but you've recently learned about Regular Expressions and believe you can 
write a script to automate this process.

Your boss has provided you a sample of the employee information.  Read in the 
employees.txt file which should be located in the Week3 folder.  Each line 
represents an employee instance.  The following things need to be updated:

1. Our domain name was too expensive, so we changed from "abc.com" to "abcompany.info"
2. Sales employees got a 5% pay raise this month for record-breaking sales numbers
3. The county split area code 123.  We are now part of area code 321.

Write a script which reads in the employee data and writes out a new file
called fixed_emps.txt with corrected information
"""

#Feel free to use regular expressions, match groups and string functions to solve
#this problem in any way you can.  Remember that, while regular expressions are very powerful,
#be careful that you don't "light a candle with a flamethrower."  In other words,
#don't use regular expressions to do something that a string function could easily do.


#%%

""" Q3.
Use your own Twitter account - or create one if you don't already have one - and
gather tweets about whatever topic you find interesting.  Try to get at least
a thousand tweets.  Load the tweets into Python, and do some analysis on them.
"""

#What are the most popular hashtags that appear in your tweets?


#What portion of your users have geo-location turned on?  Where are they located?


#What are some common words in your tweets?  Common digraphs?


#What's the username of the youngest Twitter account, and how old is it?


#What's the username of the Twitter account that has the most friends?


