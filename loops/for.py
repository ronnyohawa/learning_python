# For loop
# is Used for iterating over a sequience  either list list, tuple, dictionary,set , string
# for loop does not require an idexing variable b4 hand like the while loop
# print each fruit in a fruit list
fruits = ["apple", "orange", "peach"]

for x in fruits:
    print(x)

# Looping  through a string
for x in "banana":
    print(x)

# The break statement.
# Will stop the loop b4 it has looped throug all the items
fruits = ["apple", "orange", "cherry"]

for x in fruits:
    print(x) # tis will print appleand banana
    if x == "orange":
        break

for x in fruits:
    if x == "orange":
        break
    print(x) # this will print only apple

# The continue statement
# We can stop the current iteration of the current iteration of the loop and continue with the next

for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range function
# to loop through a set of code a specified number of times we can use the range()
# It returns a sequence of numbers starting from 0 by default and increments by 1 by default and ends at a speciefed number
for x in range(6): # the values are from 0 to 5
    print(x)

for x in range(2,6):# we have specified a starting value which is 2
    print(x)

for x in range(2,30,3): # now we have specified the increment valaue bu adding a third paraemter  which is 30
    print(x)

# Else in for loop
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    print(x)
else:
    print("Finally done")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("finally done")

# nested loop
colors = ["red","big","sour"]
fruits = ["apple","orange","cherry"]

for x in colors:
    for y in fruits:
        print(x,y)

# Pass statement
# for lops cannot be empty
for x in [1,2,3]:
    pass

