#STRING NOTES

#Strings are immutable

#Both " and ' work to denote strings

#Triple " and ' allow multiline strings

#\n is newline
#\t is tab

#+ is concatenation

#Must use str() to treat non-strings as strings
demand = 1
#request = "Hello, I would like " + demand + " cookies"  <-- Error
request = "Hello, I would like " + demand + " cookies"

#Can index individual characters in a string
"Hello"[0] == "H"

#Can index with negative numbers
"Hello"[-1] == "o" #Last character

# o  l  l  e  H  e  l  l  o
#-4 -3 -2 -1  0  1  2  3  4 

#Raw strings ignore escape characters, this is very useful for Regular Expressions
r"Open up C:\Python\fun.py" == "Open up C:\\Python\\fun.py"

#Slicing strings with [:]
"Hello"[1:3] == "el" #Read as "From character 1, up to but not including character 3"
#Negative indexes work as well
"Hello"[1:-1] == "ell"  #From character 1, up to but not including the last character
#Omitting an index indicates start at beginning / continue to end
"Hello"[:3] == "Hel"
"Hello"[4:] == "o"

#Giving an out-of-bounds index will still work
"Hello"[1:25000] == "ello"

#This makes it very simple to split a string into two parts:
greeting = "Hello"
aliengreeting = greeting[2:] + greeting[:2]

"""USEFUL STRING FUNCTIONS:

lower()
upper()
strip() <-- trim
isalpha(), isdigit(), isalnum(), isspace() <-- all chars are of specified type
startswith("other"), endswith("other")
find("other") <-- returns index of first occurrence or -1 if not found
replace("old","new")
split("delim") <-- split() splits on whitespace
join(list) <-- called-upon string used to delimit list
format(args) <-- Fill in {}s with args

"""

example = "Alfred R. Penningtonsmith"

example.lower() == "alfred r. penningtonsmith"
"Hello".upper() == "HELLO"


"    W hy not  ? ".strip() == "W hy not  ?"
"    W hy not  ? ".strip(" ?")

"123".isdigit()
"12ab3".isalpha()
"12ab3".isalnum()
"\t  \n".isspace()

example.startswith("smith")
example.endswith("smith")

example.find("fred") == 2
example.find("Fred") == -1

example.replace("n","m") == "Alfred R. Pemmimgtomsmith"

example.split() == ["Alfred","R.","Penningtonsmith"]
example.split(".") == ["Alfred R"," Penningtonsmith"] #Whitespace is kept!

words = ["Never","Say","Never"]
" ".join(words)
" Ever ".join(words)

orderitems = [("Toothpaste",)]


#Exercises:
#Use string slicing and repetition to turn "Missing Pie" into "Mississippi"
startword = "Missing Pie"
finishword = "Replace me with string functions!"
finishword == "Mississippi"

#Define a function which will take in a string and return a "crazy" string by randomly capitalizing letters
#Example Input:  "Hello!"
#Example Output: "hELlo!"

