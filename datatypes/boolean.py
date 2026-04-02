# Booleans
# Booleans represent only two values True or False. They are used to represent the truth value of an expression.

# can be used to  compare values and return a boolean value 
# e.g 5 > 3 will return True because 5 is greater than 3, while 5 < 3 will return False because 5 is not less than 3

print(10 > 9)
print(10 == 9)
print(10 < 9)

# Wen you run a condition in an if statement. the condition will be evaluated and bring true or false

a = 200
b = 50

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool("Hello")) # this will return True because the string is not empty
print(bool(15)) # this will return True because the number is not zero
print(bool(0)) # this will return False because the number is zero
print(bool("")) # this will return False because the string is empty
print(bool(None)) # this will return False because None is a special value that represents the absence of a value
print(bool([])) # this will return False because the list is empty
print(bool(())) # this will return False because the tuple is empty
print(bool({})) # this will return False because the dictionary is empty   

# One more value, or object in this case, evaluates to False, and that is if you have an object 
# that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value,
#  like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

