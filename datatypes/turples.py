# Tuples
# Are used to store multiple items in a single variable.
# The tuple is ordered so the order of the items cannot be changed 
# and unchangable meaning we cannot add, removeitems after it has been created and are written  with round brackets.

myfruits = ("apple", "mango", "orange")
print(myfruits)

# Items are indexed. the first is [0] and so on.
# It allows duplicates so we can have simillar items

# Tuple length we use the len() method to get the length of the tupple
print(len(myfruits))

# we can create a tuple with one item bu adding the comma at the nd
onetuple = ("apple",)
print(type(onetuple))

# Tuple datatypes
# it can handle any datatype and also  in one it can handle combined data
tuple1 = (1,2,3,4,5)
tuple2 = (1,"apple",True)

# tuple constructor we use this tuple()
mytuple = tuple((1, "apple", True))
print(mytuple)

# Tuple access
# we access the tuples using indexing inside a square bracket
myfruits = ("apple","mango","orange","kiwi","mellon")
print(myfruits[0]) # here we are using positive indexing

print(myfruits[-1]) # here we are using negative indexing

print(myfruits[2:4]) # here we are using the range so the second will bbe shown and the 4 will not be shown

print(myfruits[:4]) # by leaving the first empty it will start from index 0

print(myfruits[2:]) # by leaving the last empty it will go to thje end of the items

print(myfruits[-4:-1]) # we can also use negative range indexing.

# we can check if items exist we use the in keyword

if "apple" in myfruits:
    print("Yes it is available")

# Updateing tuples
# because it is not changable we can use a workaround by converting it to a list then back to a turple

myfruits = ("apple","orange")
fruitlist = list(myfruits)
fruitlist[1] = "kiwi"
myfruits = tuple(fruitlist)
print(myfruits)

# add tuple to a turple
myfruits = ("apple", "orange")
myaddtupple =("cherry",)
myfruits += myaddtupple

print(myfruits)

# Remove a item in a tupple we use the same we convert it back to a list
myfruits = ("apple", "orange")
mylist = list(myfruits)
mylist.remove("apple")

myfruits = tuple(mylist)

# To delete the full tupple we use the del keyword
deletetuple = ("apple",)
del deletetuple
# print(deletetuple) # will bring error because we have deleted the tupple


# Unpacking tuples
# when creating tuples we call that packing so we can unpack it to individual variable

fruits = ("apple","orange","cherry") # this is packing
(red,yellow,blue) = fruits # Thi is the unpacking part

print(red)
print(yellow)
print(blue)

# we can use the * astrec to unpack when the  tupple has many items but the unparckin has fewer items.
fruits = ("apple","orange","cherry","mellon","kiwi","banana")
(red,blue,*yellow) = fruits # the asteric will take all the item that do not fit and make a list for them so the yello will be a list
# we can put the asteric any where when it is in a blue it will thal all the items from the second till the secondlast item and make a list of tose item
print(red)
print(blue)
print(yellow)


# Loop tuples
# for loop 
fruits = ("apple", "orange", "cherry", "banana")

for x in fruits: # we use in keyword
    print(x)

# we can loop also using index so we use the range() and len() functions
for i in range(len(fruits)):
    print(fruits[i])

# While loop
# we use the len to detertmine the length of the tupple 
# then start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
i = 0
while i < len(fruits):
    print(fruits[i])
    i += i

# Joins tupples
fruits = ("apple", "orange")
numbers = (1,2,3)
combine = fruits + numbers
print(combine)

# we can multile tuples 
multiply = fruits * 2
print(multiply)

# The count() method returns the number of times a specified value appears in the tuple.
print(numbers.count(2))

# The index() method finds the first occurrence of the specified value.
print(numbers.index(2))
