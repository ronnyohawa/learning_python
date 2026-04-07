# Dictionary
# are used to store values in key: value pairs
# is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

mydict = {
    "brand": "Benz",
    "model": "v8",
    "Year" : "2026"
}

print(mydict)

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(mydict["brand"])

# Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# we can get the length of a dictionary  using the len()
print(len(mydict))

# we can get the type of the dataype using the type()
print(type(mydict))

# the dict() constructor
mydict2 = dict(name = "Jhon", age =  26, country = "kenya")
print(mydict2)

# Accessing items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
mycar = {
    "Brand" : "BENZ",
    "Model" : "GLE",
    "Year" : "2025"
}

print(mycar["Brand"])

# a method called get() that will give you the same result:
print(mycar.get("Brand"))

# The keys() method will return a list of all the keys in the dictionary.
print(mycar.keys())

# The values() method will return a list of all the values in the dictionary.
print(mycar.values())

# the items() method will return each item in a dictionary, as tuples in a list.
print(mycar.items())

# Check if Key Exists To determine if a specified key is present in a dictionary use the in keyword:

if "Brand" in mycar:
    print("Yes it is in the dictionary")

# Change Dictionary Items
# You can change the value of a specific item by referring to its key name:
mycar ["Year"] = "2026"
print(mycar)

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
mycar.update({"Year" : "2027"})
print(mycar)

# Add Dictionary Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
mycar ["Color"] = "Blue"
print(mycar)

# The update() method will update the dictionary with the items from a given argument. 
# If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
mycar.update({"Price": 12000000})
print(mycar)

# Remove Dictionary Items
# The pop() method removes the item with the specified key name:
mycar.pop("Model")
print(mycar)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
mycar.popitem()
print(mycar)

# The del keyword removes the item with the specified key name:
# The del keyword can also delete the dictionary completely: if we do not add the  key and square brackets 
del mycar["Color"]
print(mycar)

# The clear() method empties the dictionary:
mycar.clear()
print(mycar)


# Loop Through a Dictionary
# We use a for loop
# When looping through a dictionary, the return value are the keys of the dictionary, 
# but there are methods to return the values as well.
mycar = {
    "Brand" : "Benz",
    "Model" : "GLE",
    "Year" : 2026
}

for x in mycar: # Print all key names in the dictionary, one by one:
    print(x)

for x in mycar: # Print all values in the dictionary, one by one:
    print(mycar[x])

for x in mycar.values(): # You can also use the values() method to return values of a dictionary:
    print(x)

for x in mycar.keys(): # You can use the keys() method to return the keys of a dictionary:
    print(x)

for x,y in mycar.items(): # Loop through both keys and values, by using the items() method:
    print(x,y)


# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Make a copy of a dictionary with the copy() method:
mysimillarcar = mycar.copy()
print(mysimillarcar)

# Make a copy of a dictionary with the dict() function:

myothercar = dict(mycar)
print(myothercar)


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

Thefamly = {
    "father" : {
        "name" : "jhon",
        "age" : 58
    },
    "mother" : {
        "name" : "mary",
        "age" : 54
    },
    "son" : {
        "name" : "jane",
        "age" : 26
    }
}

print(Thefamly)

# Or, if you want to add three dictionaries into a new dictionary:

father = {
    "name" : "jhon",
    "age" : 58
}
mother = {
    "name" : "mary",
    "age" : 54
}
son = {
    "name" : "jane",
    "age" : 26
}

Thefamily = {
    "father" : father,
    "mother" : mother,
    "son" : son
}

print(Thefamily)

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(Thefamily["father"]["name"])

# You can loop through a dictionary by using the items() method like this:

for x,obj in Thefamily.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])

# Dictionary fromkeys() Method
# Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

# Dictionary setdefault() Method
#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print(x)
