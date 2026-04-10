# Fuctions
# Is a block of code which only runs when it is called.
# It can return data as a result. It helps avoiding code repetition
# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

# Creating a function
# It is defined using the def key word follored by the name of the function and parenthesis
def my_func():
    print("Hello")
# calling a function  we write its name  followed by parenthesis

my_func()
# we can call the function multiple times
my_func
my_func

# why use functions
# imagine you need to convert temp from faren to celcious several times. 
# without function you will have to write the same  calculation everytine

temp1 = 77
celcious1 = (temp1 - 32) * 5 / 9
print(celcious1)

temp2 = 95
celcious2 = (temp2 - 32) * 5 / 9
print(celcious2)

# so we can do this
def f_to_c(fa):
    return (fa - 32) * 5 / 9

print(f_to_c(77))
print(f_to_c(95))

# Return values
# Functions can send data back to the code  that called  them using  the return statement
# when a function reaches a return statement it stops executing and sends trhe results back
# If a function doesn't have a return statement, it returns None by default.
def greeting():
    return "hello there mate"

message = greeting()
print(message)

# The pass statement
def myfunc():
    pass

# Arguments 
# Parameters vs arguments
# A paremeter is the variable inside the parenthesis
# Argument is the actual value that is sent to the function when its calles
# Infor can be passed to functions as arguments
# Arguments are specified afte the function name inside the parenthesis.we can add as many as we want sepatrated with a comma

def newfunc(fname): # fname is the parameter 
    print(fname + "Doe")

newfunc("Jhon") # jhon is the argument

# Number of arguments
# If you function expects 2 arguments you must call it with exactly 2 arguments
# if you try to call the function with the wrong number you will get an error
def my_namefunc(fname,sname):
    print(fname + "" + sname)

my_namefunc("jhon", "Doe")

# Default parameter values
# we can assign  default values to parameters. if the function is called without an argument.
def my_country(name = "Kenya"):
    print("my country is " + name)

my_country() # this will use the default value
my_country("Japan")

# key word argument
# The phrase Keyword Arguments is often shortened to kwargs
# we can send arguments with the key=value pair
# using this the order of the arguments does not matter
def my_pet(animal, name):
    print("My" + animal + "s name " +name)

my_pet(animal="dog", name="culture")

# Positional Arguments
# When you call a function with arguments without using keywords
# The order matters with positional arguments
def my_pet(animal, name):
    print("My" + animal + "s name " +name)

my_pet("dog", "culture")

# Passing different Data types
# we can send any data type as an argument to a function(string, number,list, duct etc)
# the types will be precerved in the function
# sending a list
def my_list(fruits):
    for fruit in fruits:
        print(fruit)

myfruits = ["apple","orange"]
my_list(myfruits)

# Sending a dict
def my_dict(person):
    print("name: " ,person["name"])
    print("age: ", person["age"])

my_dict({"name":"emil", "age":25})

# returning diffrent data types
def my_list2():
    return ["apple","orange"]

fruits = my_list2()
print(fruits[0])
print(fruits)

# Retrning a tuple
def my_tuple():
    return (1,2)

x,y = my_tuple()
tuples = my_tuple()
print(tuples)
print("x:",x)
print("y:", y)

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments:
# With , /, you will get an error if you try to use keyword arguments:
def my_function(name, /):
    pass

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
# With *,, you will get an error if you try to use positional arguments:
def my_function(*, name):
    pass

# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
    pass


# Arbitrary Arguments - *args
# We use this if we dont know how many argument  will be passed into our function we add * b4 the parameter name
# So the function will recieve a tuple  of arguments and can access the items accordingly
# Inside the function, args becomes a tuple containing all the passed arguments:
def my_args(*kids):
    print("Type:", type(kids))
    print("First argument:", kids[0])
    print("Second argument:", kids[1])

my_args("jhon", "doe")

# using *args with regular arguments
def combine(greeting, *names):
    for name in names:
        print(greeting, name)

combine("Hello", "Jhon", "Peter", "ester")

# Practical use case for args
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(1,2,3))
print(add(1,5,7,9,5,0,8,2,4))

# find the maximum value
def max(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(max(3,7,2,9,1))

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly:

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# Using **kwargs with Regular Arguments
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Combining *args and **kwargs
# The order must be:
# regular parameters
# *args
# **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
# Unpacking Lists with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: add(1, 2, 3)
print(result)

# Unpacking Dictionaries with **
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_dict(fname="Emil", lname="Refsnes")

# Scope
# A variable is only available from inside the region it was created

# LOCAL SCOPE
# A variable created inside a functin belongs to the local scope of that function and can only be used  inside that function
# Also if the variable is in the upperf function it will work in the inner functions
def myfunc():
    x = 300
    def myinner():
        print(x)
    myinner()
myfunc()


# Gloabl Scope
# Is the variable created in the main body of the code. and belongs to the global scope
# A variable created outside of a function is global and can be used by anyone:
x = 300
def myfun():
    print(x)
myfun()
print(x)

# Naming Variables
# if we operate with the same variable name inside and otside of a function  we treat them as separetae variables. one in gloabal and one local
x = 300
def myfnct():
    x = 200
    print(x)
myfnct()
print(x) # The function will print the local x, and then the code will print the global x:

# The Global key word
# we can create the global variable inside a function using global
def myfunct():
    global x
    x = 300
myfunct()
print(x)
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300
def change():
    global x
    x=200
change()
print(x)

# NonLocal key word
# is used to work with variables inside nested functions. it makes the variable belong to the outer function
def myfunc():
    x = "jane"
    def myfunc2():
        nonlocal x
        x = "Hello"
    myfunc2()
    return x
print(myfunc())

# The LEGB RULE
# We follow the LEGB rule when looking up variable names, and searches for them in this order:
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

# Lambda Functions
# Is a small anonymus function
# It can take any number of arguments but can only have one expression
# lambda arguments : expression

# Add 10 to argument a and return the result
x = lambda a : a + 10
print(x(5))

# They can take any number of arguments
x = lambda a,b : a * b
print(x(5,6))

# summarize argu,ment a,b and cand return the result
x =lambda a,b,c : a + b + c
print(x(5,6,2))

# Why Use Lambda Functions?
# have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
    return lambda a : a * n
# use the function definition to make a function that always doubles the number you send in:
mydoubler = myfunc(2)

print(mydoubler(11))

# or, use the same function definition to make a function that always triples the number you send in:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.
# Lambda with Built-in Functions
# commonly used with built-in functions like map(), filter(), and sorted().
# Using Lambda with map()
# The map() function applies a function to every item in an iterable:
# Double all numbers in a list
numbers = [1,2,3,4,5,6]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Using Lambda with filter()
# The filter() function creates a list of items for which a function returns True:
# Filter out odd numbers from a list
numbers = [1,2,3,4,5,6,7,8,9]
odd_num = list(filter(lambda x: x % 2 !=0, numbers))
print(odd_num)

# Using Lambda with sorted()
# The sorted() function can use a lambda as a key for custom sorting:
# sort a list of tuples by the second element
students = [("Emil", 25),("Tobias", 22),("linus", 28)]
sorted_students = sorted(students, key=lambda x:x[1])
print(sorted_students)

# sort strings by length
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# Recursion
# Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to 
# slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# Simple recursive function that counts doen from 5
def countdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

countdown(5)

# Base Case and Recursive Case
# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.
# Identifying base case and recursive case:
# The base case is crucial. Always make sure your recursive function has a condition that will eventually be met.
def fuctorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * fuctorial(n - 1)
    
print(fuctorial(5))

# Fibonacci Sequence
# The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. 
# The sequence starts with 0 and 1:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# The sequence continues indefinitely, with each number being the sum of the two preceding ones.
# We can use recursion to find a specific number in the sequence:

# find the 7th number in the fiboncci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 1)
    
print(fibonacci(7))

# Recursion with Lists
# Recursion can be used to process lists by handling one element at a time:
# Calculate the sum of all elements ina list
def sumlist(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sumlist(numbers[1:])
    
mylist = [1,2,3,4,5,6]
print(sumlist(mylist))

# Find the maximum value in a list:
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

# Recursion Depth Limit
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
# Check the recursion limit:
import sys
print(sys.getrecursionlimit())

# If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
# Note Increasing the recursion limit should be done with caution. For very deep recursion, consider using iteration instead.

# Generators
# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. 
# The function only executes when you iterate over the generator.
# A simple generator function:
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

# Generators allow you to iterate over data without storing the entire dataset in memory.
# Instead of using return, generators use the yield keyword.
# The yield keyword is what makes a function a generator.
# When yield is encountered, the function's state is saved, and the value is returned. 
# The next time the generator is called, it continues from where it left off.

# Generator that yields numbers:
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

# Unlike return, which terminates the function, yield pauses it and can be called multiple times.

# Generators Saves Memory
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
# For large datasets, generators save memory:
# Generator for large sequences:

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# Using next() with Generators
# You can manually iterate through a generator using the next() function:
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# When there are no more values to yield, the generator raises a StopIteration exception:
def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
# print(next(gen)) # This will raise StopIteration

# Generator Expressions
# Similar to list comprehensions, you can create generators using generator expressions 
# with parentheses instead of square brackets:
# List comprehension vs generator expression:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# Using a generator expression with sum:
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

# Fibonacci Sequence Generator
# Generators can be used to create the Fibonacci sequence.
# It can continue generating values indefinitely, without running out of memory:

# Generate 100 Fibonacci numbers:

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

# Generator Methods
# Generators have special methods for advanced control:
# send() Method
# The send() method allows you to send a value to the generator:
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# close() Method
# The close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
print(next(gen))
gen.close()

