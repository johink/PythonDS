
#TODO:  Shorten this explanation
"""Recursion Example.
Recursion can be a useful tool, one used to approach a problem from the 
viewpoint of taking one identical step at a time until the end is reached.

Consider below, a function to add a list of numbers.  Rather than solving 
it by looping through each index and adding the value there to a sum 
variable, let's look at the structure of the data.  A list can be looked at 
as having essentially two forms:
- the empty list, []
- a list with a value in the head position, index 0, and some sub-list 
beyond that.

From this viewpoint, the list [1,2] can be looked at as the value 1 and the 
rest of the list past that [2].  This sub-list can be looked at as the value 
2 and the rest of the list, [].  The recursive code for any list function 
where we would like to act upon each value in turn follows from this 
understanding.

Our base case is when we hit the empty list, and the recursive case is when 
we still have a value sitting at the head of the list.

Coming back to the definition of our function, when we have a value at the 
head of our list, we want to return that value plus the sum of the rest of 
the list.  When only the empty list remains, we have already added all of the 
numbers in the list so we need to return a value that will not change the 
sum.
"""
def sum_list(values):
    if values == []:
        return 0
    else:
        head_value = values[0]
        tail_value = sum_list(values[1:])
        return head_value + tail_value

"""Q1.
Now that we have defined the sum_list function, let's define a function that 
does the same thing, but in a different way.  This time, we have a function 
sum_list2 that calls a helper function which computes the sum and passes that 
value along as we progress through the list.  

This value, called an accumulator, is computed as we go rather than a chain 
of addition being built up with each recursive call.  See the recursion 
practice script for more examples of recursive code that use this technique.
"""

def sum_list2(values):
    return sum_list2_helper(values, 0)

def sum_list2_helper(values, acc):
    # base case

    # recursive case


#TODO:  Some sort of scope fill in the blank problem

#TODO:  Figure out what exceptions a piece of code can throw example

#TODO:  Run-length encoding problem for algorithm implementation
