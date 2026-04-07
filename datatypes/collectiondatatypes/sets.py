# Sets
# used to store multiple items in a single variable
# it is a coolection that is unchangable, unordered, unidexed and does not alllow duplicates
# sets are wrriten with curly braces
fruits = {"apple", "orange", "banana"}
print(fruits)
# unordered so Set items can appear in a different order every time you use them, and cannot be referred to by index or key.


# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Sets cannot have two items with the same value. thus no duplicates
# Duplicate values will be ignored:
myset = {"apple",1,"orange",0,"blue","apple",True, 2,False}
print(myset)
# The values True and 1 are considered the same value in sets, and are treated as duplicates:
# The values False and 0 are considered the same value in sets, and are treated as duplicates:


# we can get the length of the set using len()
print(len(myset))

# set can be of any datatype
set1 = {"apple","orange"}
set2 = {1,2}
set = {True,False}
# it can combime all the datatypes
set4 = {"apple",1,"orange",0,"blue","apple",True, 2,False}

# we can use the type() to get the type
print(type(set4))

# The set constructer to create sets also set()
set5 = set(("apple",1,False))
print(set5)

#Note 
# Set items are unchangeable, but you can remove items and add new items.


# Accesing items in a set
# Because there is no index ina set we use for loop to access the items 
set4 = {"apple",1,"orange",0,"blue","apple",True, 2,False}
for x in set4:
    print(x)

# using the in keyword to check if an item is in a set we can also use not in key word
print("apple" in set4)
print("banana" not in set4)

# Adding an item in a set we use the add() method
fruits = {"apple","orange"}
fruits.add("banana")
print(fruits)

# we can combine one set to another using the Update() method also we can add  lists, and others using  the update methode
fruits = {"apple", "orange"}
numbers = {1,2}
fruits.update(numbers)
print(fruits)

# Removing items in set
# we can use the remove() method to remove specif item that is in the set if its not available it will bring an error

fruits = {"apple", "orange", "banana","cherry"}
fruits.remove("cherry")
print(fruits)

# we can use the discard() to remove a known item but this will not bring an error if its not available
fruits = {"apple", "orange", "banana","cherry"}
fruits.discard("apple")
print(fruits)

# You can also use the pop() method to remove an item, but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
fruits = {"apple", "orange", "banana","cherry"}
fruits.pop()
print(fruits)

# The clear() method empties the set:
fruits = {"apple", "orange", "banana","cherry"}
fruits.clear()
print(fruits)

# The del keyword will delete the set completely:
fruits = {"apple", "orange", "banana","cherry"}
del fruits
print(fruits) # this will bring error

# Looping sets
# we use for loop
fruits = {"apple",1,"banana"}

for x in fruits:
    print(x)

# We can Join sets using many methods
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# UNION
# union() returns a new set with all the values combined
set1 ={1,2,3}
set2 ={"a","b","c"}
set3 = set1.union(set2)
print(set3)

# we can also use | operator instead of the union() method, and you will get the same result.
set4 = set1 | set2
print(set4)

# Join Multiple Sets
set1 ={"a","b","c"}
set2 ={1,2,3}
set3 ={"john","elena"}
set4 = set1.union(set2,set3)
set5 = set1 | set2 | set3
print(set4)
print(set5)

# Join a Set and a Tuple 
# The union() method allows you to join a set with other data types, like lists or tuples.
# Note: The  | operator only allows you to join sets with sets, and not with other data 
# types like you can with the  union() method.
set1= {1,2,3}
tuple1 = (4,5,6)
set2 = set1.union(tuple1)
print(set2)

# UOPDATE
# Update() method inserts all items from one set into another.
set1 = {1,2,3}
set2 ={4,5,6}
set1.update(set2)
print(set1)


# INTERSECTION
# Intersection() it keeps only duplicates in both sets. 
# return a new set, that only contains the items that are present in both sets.
set1 = {"apple","banana","cherry"}
set2 = {"microsft", "facebook", "apple"}
set3 = set1.intersection(set2)
print(set3)
set4 = set1 & set2 # You can use the & operator instead of the intersection() method, and you will get the same result.
print(set4)

# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.
set1.intersectio_update(set2)
print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# DIFFRENCE
# The difference() method will return a new set that will contain only the items 
# from the first set that are not present in the other set.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.difference(set2)
print(set3)
set4 = set1 - set2 # You can use the - operator instead of the difference() method, and you will get the same result.
print(set4)

# The difference_update() method will keep the items from the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.
set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set5 = set1.symmetric_difference(set2)
print(set5)
set6 = set1 ^ set2 # You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
print(set6)

# The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
set1.symmetric_difference_update(set2)
print(set1)

# FROZEN SET
# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.

# Use the frozenset() constructor to create a frozenset from any iterable.
x = frozenset({"apple","banana","cherry"})
print(x)
print(type(x))

# Set copy() Method
y = set5.copy()
print(y)

# Set isdisjoint() Method
# Return True if no items in set1 is present in set2:
z = set1.isdisjoint(set2)
print(z)

# Set issubset() Method
# Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(y)
# As a shortcut, you can use the <= operator instead, see example below.
print(x <= y)

# Set issuperset() Method
# Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)
# As a shortcut, you can use the >= operator instead, see example below.
print(x >= y)

# Set < (less than) Method
# Returns False even if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"c", "b", "a"}

z = x < y
print(z)

# Returns True because all items of set x is present in the larger set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x < y
print(z)

# Set > (greater than) Method
# Returns False even if all items in set y are present in set x:
x = {"a", "b", "c"}
y = {"c", "b", "a"}

z = x > y
print(z)

# Returns True because all items of the smaller set y is present in the set x:
x = {"a", "b", "c"}
y = {"b", "a"}

z = x < y
print(z)
