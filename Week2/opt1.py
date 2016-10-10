
"""Q1.
Consider the following function and function signature.  The goal of this 
problem is to complete the helper recursive function so that the sum of the 
values in the list is computed.  

For example:
-sum_list2([1,2,3]) >> returns 6
-sum_list2([])      >> returns 0

See recursion.py in practice scripts for another example of sum_list and 
other recursive function examples/problems.
"""

def sum_list2(values):
    return sum_list2_helper(values, 0)

def sum_list2_helper(values, acc):
    raise NotImplementedError("Need to implement this function.")
    # base case

    # recursive case


assert sum_list2([1,2,3,4,5,6,7,8,9,10]) == 55



#TODO:  Some sort of scope fill in the blank problem

#TODO:  Figure out what exceptions a piece of code can throw example


"""Q2.
Implement the run-length encoding algorithm for strings.  This is a basic, 
lossless compression algorithm that shortens the string by replacing long 
repetitions of characters with a character and number pair that denote the 
length.

For instance the string "aaaabbbcddeeeee" can be encoded as "a4b3cdde5", 
turning a length 15 string into a length 9 one.
Note that dd is not replaced by d2 because it does not save any space, and 
similarly c is not replaced by c1 because its encoding takes up more space!

This encoding will require you to keep a count of how many times a character 
has occurred as you loop through the string, and output the encoded version 
once you see a new character.

Here is Wikipedia's article that has another example and a bit more 
explanation:
https://en.wikipedia.org/wiki/Run-length_encoding
"""

def rl_encode(string):
    raise NotImplementedError("Need to implement this function.")

assert rl_encode("aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbceeeeeeeeeaaaaaaaaaaaaa") == "a21b12ce9a13"


"""Q3.
Implement the reverse of the last problem, the run-length decoding algorithm. 
Given a string compressed in that format, return the original string.  No use 
having a compression algorithm if you cannot reverse it!
"""


def rl_decode(string):
    raise NotImplementedError("Need to implement this function.")

assert rl_decode("a21b12ce9a13") == "aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbceeeeeeeeeaaaaaaaaaaaaa"

