# IF STATEMENT
# Python supports use of logical conditions from math
# Equals a == b, Not Equals a!=b, less than a < b, less or equal to a<=b, greater than a>b, greater than or equal to a>=b
# This conditions can be used in several  ways in if statements and loops.
# an if statement uses the if keyword
#An if statement evaluates a condition that results in true or false. if the condition is true the code block inside if statement is executed. if false the block is skipped
# 
a = 200
b = 150

if a > b:
    print("a is greater than b")


# using variables in conditions
# Boolean values can be used directly in the if statements without comparision operators
is_loged_in = True
if is_loged_in:
    print("Welcome back to the system")

# We can evaluate many types of values as True or False in an if statemen. 
# Zero(0), empty strings(""), None and empty collections are treated  as False. Everything else is True

# ELIF STATEMENT
# The elif keyword is just saying if the previous conditions were not true  then try this condition.
# So this checks if a block is true and runs that block.
# We can have many elif statements as we need.
# we use it when we have  multiple  mutually  exclusive conditions to check e.g grades or days of the week
if a < b:
    print("a is less tha b")
elif a > b:
    print("a is greater than b")

# Projoject for days of the week
day = 3

if day == 1:
    print("monday")
elif day == 2:
    print("Teusday")
elif day == 3:
    print("Wenesday")

# ELSE STATEMENT
# The else keyword catches anything which isnt caught by the preceding conditions
# we can use it to show errors
else:
    print("We cannot determine the date")


# LOGICAL OPERATORS
# are used to combine  conditional statements.
# and - returns true if both  statements are true
a = 200
b = 33
c = 500
if a > b and c > a:
    print(" Both conditions are true")

# or - returns true if one condtion is true.
if a > b and b > c:
    print("At least one condition is true")

# not - is used to reverse the result of a conditional statement
if not a < b:
    print("b is greater than a")

# we can combime multiple operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 and age > 65) and is_student or has_discount_code:
    print("Discount applies")

username = "Ronny"
password = "secret123"
is_verified = True

if username and password and is_verified:
    print("Login successfull")
else:
    print("Invalid details")

score = 85

if score >= 0 and score <=100:
    print("valid score")
else:
    print("Invalid score")

temp =45
is_raining = True
is_weekend = True

if (temp > 20 and not is_raining) or is_weekend:
    print("Have a great day outside")

# NESTED IF
# You can have if staetments inside if staements.
# Sometimes nested if statements can be simplified using logical operators like and. The choice depends on your logic.
x = 41

if x > 10:
    print("above 10")
    if x > 20:
        print("Above 20")
    else:
        print("Not above 20")

# Login validation logic

username = "ron"
password = "secret"
is_verified = True

if username:
    if password:
        if is_verified:
            print("Login success")
        else:
            print("Not verified")
    else:
        print("wrong password")
else:
    ("Username required")

# Grade callculation
grade = 92
credit = 5

if grade >= 90:
    if credit > 0:
        print("A+")
    else:
        print("A")
elif grade >= 80:
    print("B")
else:
    print("Fail")

# PASS STATEMENT
# if satements cannot be empty  but if for some reason you  have an if statement and no content  we put the pass to avoid getting an error
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
a = 20
b = 30

if a > b:
    pass

# The pass statement is useful in several situations:
# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later

