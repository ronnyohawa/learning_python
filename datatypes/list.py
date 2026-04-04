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


