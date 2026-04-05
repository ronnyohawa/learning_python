# Is used to store multiple items in a single variable. 
# Lists are created using square brackets [] and the items are separated by a comma.

fruits = ["apple", "bannana", "cherry"]
print(fruits)

# list items are ordered, changeable and allow duplicates
# what we mean by ordered is that the items have a defined order and it will not change. so when we add a new item to the list it will be inserted at the last part of the list.
# Changerebale means we can change, add or remove items in a list after it has been created.
# Allow duplicates means that we can have two items with the same value in a list.

# list items are indexed and you can access them by referring to the index number. the first is [0], the second is [1].
print(fruits[0])

# List length is gotten by using the len() function.
print(len(fruits))

# List items can be of any data type and can be mixed data types.
list1 = ["apple", "bannana"]
list2 = [1,2,3]
list3 = [True, False]
list4 = ["apple", 1, True]

# list type() function is used to determine the data type of a list which is categorized as an object with data type list
print(type(fruits))

# The list() constructer can be used to create a list.
fruits = list(("apple", "bannana",))
print(fruits)

# Accessing lists items
# positive indexing starts from 0 and so on.
print(fruits[0])

# negative indexing starts from -1 and onwards. as -1 is the last item, -2 is the second last item and so on.
print(fruits[-1])

# Range of indexing  can be specied by using the colon : operator. 
# the first value is the starting index and the second value is the ending index. 
# the range of indexing will include the starting index but not the ending index.
print(fruits[0:2])

# by leaving the first value empty  it will start from the start of the list.
print(fruits[:2])

# by leaving the secont value empty it will go to the end of the list.
print(fruits[0:])

# We can also use negative indexing in range.
# the first value is the starting index and the second value is the ending index.
print(fruits[-2:-1])

# checking if an item exist in a list we use the in keyword
if "apple" in fruits:
    print("Yes, is in the list")

# Changing list items. we can change a specific item using it index.
fruits[0] = 'orange'
print(fruits)

# change a range of items  is done using the range.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits[1:3] = ["blackcurrent", "watermelon"]
print(fruits)

# what if i want to change  3 items in a lis of 6 items. 
# we can do that by specifying the range of items we want to change 
# and then specify the new items in a list.
fruits[1:4] = ["blackcurrent", "watermelon", "grapes"]
print(fruits)

# if you place more items than you are replacing, 
# the new items will be inserted in the list at the specified index 
# and the rest of the items will be shifted to the right.
fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["blackcurrent", "watermelon"]
print(fruits)

# if yore insert less items than you are replacing, 
# the new items will be inserted in the list at the specified index 
# and the rest of the items will be shifted to the left.
fruits[1:3] = ["blackcurrent"]
print(fruits)

# to insert items without replacing any of the exosting  we use the insert() method. 
# the insert method takes two arguments, the first is the index where you want to insert the item and the second is the item you want to insert.
fruits.insert(2, "watermelon")
print(fruits)

# To add items at the end of the list we use the append() method. it oly takes one argument which is the item you want to add.
fruits.append("grapes")
print(fruits)

# we can also add items from another list to the current list ung the extend() method. 
# it takes one argument which is the list you want to add to the current list.
# the extend() method adds the items of the specified list to the end of the current list.
fruits2 = ["kiwi", "mango"]
fruits.extend(fruits2)
print(fruits)

# we can also add any iterable object to the current list using the extend() method. 
# eg a tuple, a set, a dictionary etc.
fruits = ["apple", "banana", "cherry"]
fruitstuple = ("kiwi", "orange")
fruits.extend(fruitstuple)
print(fruits)


# Remove Items from a list
# We can use the remove() method to remove a specified item from the list. 
# it takes one argument which is the item you want to remove.
# Note it removes the first occurence of the item.
fruits.remove("banana")
print(fruits)

# we use  the pop() method to remove a item in the list by specifing its index.
# if you do not specify the index it will remove the last item in the list.
fruits.pop(1)
print(fruits)

# also the del keyword can be used to remove an item in the list by specifying its index.
del fruits[0]
print(fruits)

# also the del keyword can be used to remove the entire list.
del fruits 

# we can also use clear() method to remove all the items but the list still exists.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)


# Looping List
# For loop is used to loop through items in a list
fruits= ["apple", "bannana", "cherry"] # we create first the variable fruits and assign it a list of items.
for x in fruits: # we use the for loop to loop the items in the list and assign each item to the variable x
    print(x)

# we can also loop using index of the list items using the range() and len() functions

for i in range(len(fruits)): # we use range() function to generate a sequence of numbers from 0 to the length of the list 
    #and assign it to the variable i
    print(fruits[i]) # we use the variable i to access the items in the list using their index and print them

# While Loop in a list
fruits = ["apple", "banana", "cherry"]
i = 0 # we create a variable i and assign it the value of 0

while i < len(fruits):
    print(fruits[i])
    i += 1 # we increment the value of i by 1 in each iteration of the loop


# sorting of lists
# sort() method is used to sort the items in a list in assending order by defauld.
fruits = ["banana", "cherry", "apple"] 
fruits.sort()  # this will sort the list in alphabetical order
print(fruits)

# to sort in decending order we use the reverse parameter and set it to true
fruits.sort(reverse= True)
print(fruits)

# Case sensitive sort the sort function will tend to sort the caps  items first b4 the small lettes to fix 
# that we can use the key parameter and set it to str.lower to sort the items in a case insensitive way.
fruits = ["banana", "Cherry", "apple"]
fruits.sort(key= str.lower)
print(fruits)

# customize my sort function
# we can also create our own sort function by defining a function and then using it as the key parameter in the sort() method.
def myfunc(n):
    return abs(n-50) # this function will return the absolute value of the diffrence between the number and 50
# what is abs function? the abs() function is a built-in function in python that returns the absolute value of a number. 
# the absolute value of a number is the distance of the number from zero on the number line. 
# for example, the absolute value of -5 is 5 and the absolute value of 5 is also 5. 
# so in our myfunc() function we are calculating the distance of each number from 50 
# and then sorting the numbers based on that distance.

mynumbers = [100, 50, 65, 82, 23]

mynumbers.sort(key= myfunc) # this will sort the numbers based on their distance from 50
print(mynumbers)

# Coping of list
# copy() method is used to copy a list. it creates a new list with the same items as the original list
fruits = ["apple","banana", "cherry"]
myfruits = fruits.copy() # this will create a new list myfruits with the same items as fruits
print(myfruits)

# list() can also be used to copy a list. it creates a new list with the same items as the original list
myfruits2 = list(fruits) # this will create a new list myfruits2 with the same items as fruits
print(myfruits2)

# The slice operator : cana also be used to copy a list. it creates a new list with the same items as the original list
myfruits3 = fruits[:] # this will create a new list myfruits3 with the same items as fruits
print(myfruits3)

# Joining Lists
# + we can join two list using the + operator. it will create a new list that contains all the items from both lists.
list = [1,2,3,4]
list2 = [5,6,7]

list3 = list + list2 # this will create a new list list3 that contains all the items from list and list2
print(list3)

# append() method can be used to add the items of one list to the end of another list. it will modify the original list.
list = [1,2,3,4]
list2 = [5,6,7]

for x in list2:
    list.append(x) # this will add each item from list2 to the end of list
print(list)

# extend() method can also be used to add the items of one list to the end of another list. it will modify the original list.
list = [1,2,3,4]
list2 = [5,6,7]

list.extend(list2) # this will add all the items from list2 to the end of list
print(list)

