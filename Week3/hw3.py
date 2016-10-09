

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
Write the negation of the previous regex, one which only matches IMPROPER 
formatted identifiers.  Assume that improperly identified terms are:  
-3 or 4 capital letters,
-a space,
-any 3 digit number,
-any capital letter
"""

course_list = ['ART 156', 'ART149G', 'ART 196', 'ART 212L', 'ART 245', 'ART 227', 'ART 251', 'ART336', 'ARTTT 377', 'ART 381', 'BIO 134', 'BIO2 105', 'BIO 149S', 'BIO 223', 'BIO 244H', 'BIO 250', 'BIO 233T', 'BIO 384', 'BIO 364', 'BIO 305', 'CSC 126D', 'CSC 114', 'CSC 130E', 'CSC 285', 'CS 284G', 'CSC 236', 'CSC 265', 'CSCI 357', 'CSC 304S', 'CSC 388', 'GTCS 198H', 'GTCS 171', 'GTCS 004', 'GTCS 251S', 'GTCS 280', 'GTCS 285W', 'GTCS 218', 'GTCS 365', 'GTCS 488', 'GTCS 342P', 'LIN 173', 'LIN 024', 'LIN 150', 'LIN 290', 'LIN 234', 'LIN 248L', 'LIN 550', 'LIN 326', 'LIN 349', 'LIN 349L', 'MTH 169', 'MTH188', 'MTH 113', 'MTH 251H', 'MTH 248', 'MTH 200', 'MTH 232', 'MTH 365H', 'MTH 388', 'MTH 371', 'POL 170S', 'POL 102', 'POLs 104', 'POL 281', 'POL 240H', 'POL 285', 'PO 256', 'POL 326', 'POL 383', 'POL 369X', 'ROM 191', 'ROM 119Y', 'ROM 191', 'ROM 217', 'ROM 280HI', 'ROM 237', 'ROM 219S', 'ROM 350', 'ROM 314', 'ROM 318']

answer = []

assert answer.sort() ==  ['ART149G', 'ART336', 'ARTTT 377', 'BIO2 105', 'BIO 233T', 'CSC 126D', 'CSC 130E', 'CS 284G', 'GTCS 004', 'GTCS 285W', 'GTCS 488', 'GTCS 342P', 'LIN 024', 'LIN 550', 'MTH188', 'POLs 104', 'PO 256', 'POL 369X', 'ROM 119Y', 'ROM 280HI'].sort()
