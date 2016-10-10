"""Recursion Example.
Recursion can be a useful tool, one used to approach a problem from the 
viewpoint of taking one identical step at a time until the end is reached.
What that step entails is dependent on the data that the function is 
recursing over.

Consider below, a function to sum up a list of values.  Rather than solving 
it by looping through each index, adding that value to a sum variable, then
returning that at the end let's look at the structure of the data.

Instead of looking at a list as a series of indexed positions, it can be 
looked at as having to forms:
- the empty list, []
- a list with a value in the head position, index 0, and some sub-list in the 
tail position beyond that

Through this lense, the singleton list [3] can be look at as the value 3 
in the head position, and the empty list, [], in the tail position.  [1,2] 
can be looked at as 1 in head position and the sub-list [2] in the tail 
position, which can similarly be broken down.

With this understanding of how a list can be broken down step-by-step until 
we reach the empty list, a recursive definition for a function acting on each 
value in the list in turn follows nicely.  Our base case is when we reach 
the empty list, and the recursive case is when we have some value at the head 
of the list.

Coming back to the sum_list function, let's look at each case.  When only the 
empty list remains we have already summed up all of the numbers in the list. 
In the other case we want to add one more number to our sum and repeat the 
operation on the rest of the list.
"""

def sum_list(values):
    if values == []:
        return 0
    else:
        head_value = values[0]
        tail_value = sum_list(values[1:])
        return head_value + tail_value

"""
Can you think of lists of other datatypes that sum_list would work on?  Why 
does it work on other datatypes beyond integers and floats?
"""


"""Binary Search Trees.

Below is a given implementation of a binary search tree, a common data 
structure in computer science.  Recursion on lists is not an effecient 
way to calculate functions like the sum of a list in Python.  However, 
recursive binary search tree operations are a reasonable option.

The BSTree has the following properties:
-It is a tree, which consists of a root node that holds some data and a 
    connection to it's "children" nodes that are of the same form
-Each node is binary, only having two "children" nodes, left and right
-The tree is ordered using this search property, where all of the nodes 
    to the left of the current node have data that is less than the value of 
    the data in the current node, and all of the nodes to the right have a  
    greater value.

Consider the following example, where () is an empty node and >> shows a 
visualization of the tree:
test = BSTree()
    ()

test.insert(5)
   (5)
  /   \
 ()   ()

test.insert(3)
   (5)
  /   \
(3)   ()

test.insert(4)
       (5)
      /   \
    (3)   ()
   /   \
  ()   (4)

test.insert(7)
         (5)
      /       \
    (3)       (7)
   /   \     /   \
  ()   (4)  ()   ()

test.insert(9)
         (5)
      /       \
    (3)       (7)
   /   \     /   \
  ()   (4)  ()   (9)

The search function follows from the search property, bisecting the tree at 
each step until it finds the data or "falls of the end" of one of the tree 
branches.
"""
class BSTree:

    def __init__(self):
        self._root = None

    class TreeNode:
        def __init__(self, data, left = None, right = None):
           self.data = data
           self.left = left
           self.right = right 

    def insert(self, data):
        self._root = self._insert(data, self._root)

    def _insert(self, data, node):
        if node == None:  return self.TreeNode(data)
        elif data < node.data:  node.left = self._insert(data, node.left)
        elif data > node.data:  node.right = self._insert(data, node.right)
        else:  node.data = data
        return node

    def search(self, data):
        return self._search(data, self._root)

    def _search(self, data, node):
        if node == None:  return False
        elif data < node.data:  return self._search(data, node.left)
        elif data > node.data:  return self._search(data, node.right)
        else:  return True

    def is_empty(self):
        return self._root == None

    def min(self):
        return self._min(data, self.root)

    def _min(self, node):
        raise NotImplementedError("The minimum function needs to be defined")

    def max(self):
        return self._max(data, self.root)

    def _max(self, node):
        raise NotImplementedError("The maximum function needs to be defined")

"""Coding exercise.
Define the min and max functions for BSTree, recursively.  Look at the other 
functions as an example for understanding how to step through the tree 
recursively.

Consider how values are ordered in the tree, and where these values will be 
located.
"""

tree = BSTree()
tree.insert(5)
tree.insert(10)
tree.insert(9)
tree.insert(8)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(12)


assert tree.min() == 1
assert tree.max() == 12
