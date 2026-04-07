
# Now we will  dive deep to the numeric types
# as we know we have three types  int, float and complex

# so w start with int
# int is a whole number either negative or positve with no decimal point of unlimited length eg 1,-1,2,-2

x = 2
y = -3
z = 35753893635

print(type(x)) # this will print the type of the variable x  which is int
print(type(y)) # this will print the type of the variable y
print (type(z)) # this will print the type of the variable z


# Floating point numbers
# fload is a negative or positive number with  a decimal point or in exponential form e.g 3.14, -3.14, 1.5e2

x = 3.14
y = -2.15
z = 1.5e2
a = 13E2
b = 35e2

print(type(x)) # this will print the type of the variable x which is float
print(type(y)) # this will print the type of the variable y
print(type(z)) # this will print the type of the variable z
print(type(a)) # this will print the type of the variable a
print(type(b)) # this will print the type of the variable b

# Complex numbers 
# a complex number is a number that has a real number and an imaginary number j e.g 2 + 3j, -1 - 2j, 3j
x = 2 + 3j
y = -1 + 2j
z = 3j

print(type(x)) # this will print the type of the variable x which is complex
print(type(y)) # this will print the type of the variable y
print(type(z)) # this will print the type of the variable z

# Type Conversion
# type conversion is where by we change the data type of one variable to another e.g int to float, int  to  complex , float to int, float to complex
# using this methods  int(), float(), and complex()
x = 2
y = 3.14
z = 2 + 3j

# float to int
a = int(y)
print(a)

# int to float
b= float(x)
print(b)

# int to complex
c = complex(x)
print(c)

# float to complex
d = complex(y)
print(d)

# NOTE : you cannot convert complex number to another data  type because it has both real and imaginary part and it will cause loss of data if we try to convert it to another data type

# RANDOM NUMBER GENERATION
# python does not have an inbuild random number  generator  so we use  the random module to generate them

import random
print(random.randrange(1,10)) # this will generate a random number between 1 and 10
print(random.randint(1,10)) # this will generate a random number between 1 and 10 inclusive
print(random.random()) # this will generate a random number between 0 and 1
print(random.uniform(1,10)) # this will generate a random number between 1 and 10 with decimal point

