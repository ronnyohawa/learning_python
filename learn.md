# Python Introduction
# What can Python do?
used on a server to create web applications.
used alongside software to create workflows.
used to handle big data and perform complex mathematics.

# Why Python?
works on different platforms
has a simple syntax
write programs with fewer lines
runs on an interpreter system, meaning that code can be executed as soon as it is written
can be treated in a procedural way, an object-oriented way or a functional way.

# Python Syntax
uses new lines to complete a command
relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes.


# Python Install
Many  machines have python installed e.g ubuntu and mac os
To check if Python is installed we use this command in the command line 
Python –version —------------ windows os
Python3 ---version  —------------ linux and mac os

 If you are using an editor like vs code you can check the  version  with  this
Import sys

print(sys.version)

# To create a python project
First i like to start with a virtual environment

As i am using mac i use this command
Python3 -m venv venv

Then to activate the environment i use this command
Source venv/bin/activate
Also we can run the  python in the terminal by using this command
learning_python$ python
After that  we can run any python command in the  terminal e.g
Python 3.12.3 (main, Mar  3 2026, 12:15:18) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello")
hello

To exit from it we use the exit command
>>> exit()


You can also create a python file  using the python commande.g
Python learning.py

# Python Syntax
# Python Indentation
refers to the spaces at the beginning of a code line.
uses indentation to indicate a block of code.

if 5 > 2:
  print("Five is greater than two!")

Python will give you an error if you skip the indentation:


# Comments
Comments start with a #, and Python will render the rest of the line as a comment

#This is a comment.
print("Hello, World!")

# Multiline Comments
Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!") 
Python Statements
these programming instructions are called statements.

print("Python is fun!") 

Many Statements
Most Python programs contain many statements.
The statements are executed one by one, in the same order as they are written:
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!") 



# Variable Names
must start with a letter or the underscore character
cannot start with a number
can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
are case-sensitive (age, Age and AGE are three different variables)
cannot be any of the Python keywords.

# Multi Words Variable Names
There are several techniques you can use to make them more readable:
Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"
Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"
Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"

# Python Variables
a variable is created when you assign a value to it

x = 5
y = "Hello, World!"

You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y)) 


# Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# Global Variables
Variables that are created outside of a function are known as global variables.
can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

# The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 


# Python Output
you can use the print() function to display text or output values:
ust be inside quotes. You can use either " double quotes or ' single quotes:
By default, the print() function ends with a new line.
If you want to print multiple words on the same line, you can use the end parameter:

print("Hello World!", end=" ")
print("I will print on the same line.")

You can also use the print() function to display numbers:
we don't put numbers inside double quotes:

print(3)
print(358)
print(50000)

You can also do math inside the print() function:
print(3 + 3)
print(2 * 5)

You can combine text and numbers in one output by separating them with a comma:

print("I am", 35, "years old.")

In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# Python Data Types

Text Type:
str

Numeric Types:
int, float, complex

Sequence Types:
list, tuple, range

Mapping Type:
dict

Set Types:
set, frozenset

Boolean Type:
bool

Binary Types:
bytes, bytearray, memoryview

None Type:
NoneType

# Getting the Data Type
You can get the data type of any object by using the type() function:
x = 5
print(type(x))

# Setting the Data Type
the data type is set when you assign a value to a variable:

x = "Hello World"
str

x = 20
int

x = 20.5
float

x = 1j
complex

x = ["apple", "banana", "cherry"]
list

x = ("apple", "banana", "cherry")
tuple

x = range(6)
range

x = {"name" : "John", "age" : 36}
dict

x = {"apple", "banana", "cherry"}
set

x = frozenset({"apple", "banana", "cherry"})
frozenset

x = True
bool

x = b"Hello"
bytes

x = bytearray(5)
bytearray

x = memoryview(bytes(5))
memoryview

x = None
NoneType





