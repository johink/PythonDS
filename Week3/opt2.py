from functools import reduce

# lambda, map, reduce, filter, list comprehensions

"""Q1.
Define the sum_list function(description in opt1.py and recursion.py) using 
only the reduce function and a lambda function.
"""

def sum_list(values):
    raise NotImplementedError("Need to implement this function")

assert sum_list[1,2,3,4,5,6,7,8,9,10] == 55


"""Q2.
Define the double_all function two ways: 
-using the map function and a lambda function
-using a list comprehension with no lambda function

double_all takes in a list of values and multiplies them all by 2
"""

def double_all_map(values):
    raise NotImplementedError("Need to implement this function")

def double_all_comprehension(values):
    raise NotImplementedError("Need to implement this function")

in_list = [1,2,3,4,5]
out_list = [2,4,6,8,10]

assert double_all_map(in_list) == out_list
assert double_all_comprehension(in_list) == out_list


"""Q3.
Define a function that removes all of the vowels from a given string, using 
the filter function and a lambda function.

Filter returns an iterable object, so to convert it back to a string we use 
''.join(filter_object).
"""

def no_vowels(in_string):
    filter_return = []      # replace this with the call to filter
    return ''.join(filter_return)
