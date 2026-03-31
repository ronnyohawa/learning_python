# Strings
# A string is a sequence of characters  enclosed in either a single quotation or double qutation marks e.g "Hello", 'Hello', "This is a string", 'This is also a string'

print("Hello")
print('Hello')
print("This is a string")
print("Hello, my name is Ronny")
print("Hello 'Ronny'")
print('Hello "Ronny"')

# assign a string to a variable
a = "hello"
print(a)

# Multiline string 
# we can assign a multiline string using triple quotes e.g """This is a multiline string""" or '''This is also a multiline string'''
b =  """ this is 
is a
 string that spans multiple lines"""
print(b)

# Strings are Arrays
# Python does not have a character data type, a single character is simply a string with a length of 1.
# we can access the characters in a string using indexing e.g string[index] where index starts from 0 for the first character, 1 for the second character and so on. we can also use negative indexing to access the characters from the end of the string e.g string[-1] for the last character, string[-2] for the second last character and so on.

b = "Hello, world"

print(b[0]) # this will print the first character of the string which is H
print(b[1]) # this will print the second character of the string which is e
print(b[2]) # this will print the third character of the string which is l
print(b[-1]) # this will print the last character of the string which is d
print(b[-2]) # this will print the second last character of the string which is l
print(b[-3]) # this will print the third last character of the string which is r

# Looping a string because its just an array of characters using for loop

for i in b:
    print(i) # this will print each character of the string on a new line

for i in "Hello":
    print(i)

# String Length 
# we use the len() function to get the length of a string e.g len(string)

c = "Hello, world"
print(len(c)) # this will print the length of the string which is 12

# Check String
# we can check if a phrapse is available in the  text using the in keyword e.g "phrase" in string

d = "We are travelling next week arte you free"

print("free" in d) # this will print True because the word free is in the string

# we can also use if to check the phrase

if "free" in d:
    print("yes, free is in the string")

# Check String is not
# we can check if a phrase is not in the string using the not in keyword e.g "phrase" not in string

print("busy" not in d) # this will print True because the word busy is not in the string

# we can also yse if to check the phrase
if "busy" not in d:
    print("yes, busy is not in the string")


# String Slicing
# we can return a range of characters in a string using slicing e.g string[start:end]
#  where start is the index of the first character and end is the index of the last character

e = "Hello, world!"
print(e[2:5]) # this will print the characters from index 2 to index 4 which is llo

# Slice From the Start
# By leaving out the start index, the range will start at the first character:

print(e[:5]) # this will print the characters from the start to index 4 which is Hello

# Slice To the End 
# byleaving out the end index, the range will go to the end:

print(e[2:]) # this will print the characters from index 2 to the end which is llo, world

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# in negative indexing the last character is -1 the second last is -2 and so on

print(e[-5:-2]) # this will print the characters from index -5 to index -3 which is.

# Modify Strings
# Upper Case
# we can convert a string to upper case using the upper() method e.g string.upper()
f = "Hello, world!"
print(f.upper()) # this will print the string in upper case which is HELLO, WORLD!

# Lower Case
# we can convert a string to lower case using the lower() method e.g string.lower()

print(f.lower()) # this will print the string in lower case which is hello, world!

# Remove whitespace
# we can remove whitespace from the beginning and the end of a string using the strip() method e.g string.strip()

g = " Hello, world! "
print(g.strip()) # this will print the string without the whitespace which is Hello, world!

# Replace String
# we can replace a string with another string using the replace() method e.g string.replace("old","new")
h = "Hello, world!"
print(h.replace("H","j")) # this will replace the letter H with j and print jello, world!

# Split String
# we can split a string into a list of substrings using the split() method e.g string.split("separator") where separator is the character or string that we want to use as a separator
i ="Hello world!"
print(i.split(" ")) # this will split the string into a list of substrings using the space as a separator and print ['Hello', 'world!']

# String Concatenation
# we can concatenate two strings using the + operator e.g string1 + string2
j = "Hello"
k = "world!"
l =j+k
print(l) # this will concatenate the two strings and print Helloworld!
l = j + " " + k
print(l) # this will concatenate the two strings with a space in between and print Hello world
print(j + " " + k) # this will print Hello world!

# String Formating
# We can formart strings using the format() method e.g string.format(value1, value2, ...) 
# or using f-strings e.g f"string {value1} string {value2} ..."

# F-Strings
# It allows yo to formart selected part of the string by placing an f infront of the string
txt = f"The price of this product is 100 dollars"
print(txt) # this will print the string as it is because there are no variables to format

# Placeholders and modifiers
# to formart values in an f string we add placeholders and modifiers in the string e.g {value:modifier} 
# where value is the variable that we want to format 
# and modifier is the type of formatting that we want to apply to the variable

price = 100
txt = f"The price of this product {price} dollars"
print(txt) # this will print the string with the value of the variable price which is 100 dollars

# A modifier is added by including a colon : after the variable name, followed  by the formating type you 
# want to apply to the variable e.g {value:modifier}

text = f"The price of this product is {price:.2f} dollars"
print(text) # this will print the string with the value of the variable price formatted to 2 decimal places 
# which is 100.00 dollars

# Perform operations in the f string

price =100
tax = 0.15

txt =f"The total price of this product is {price + (price * tax)} dollars"
print(text)

# Perform if else in the f strings
price = 100

text = f"the price of the product is {'expensive' if price >50 else 'cheap'}"
print(text) # this will print the string with the value of the variable price evaluated in the if else statement which is expensive because the price is greater than 50

# Executing functions in F strings

fruit = "apple"

text =f"The name of this fruit is an {fruit.upper()}"
print(text)

# string formart method
# The format() method can still be used, but f-strings are faster and the preferred way to format strings.
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Escape characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# \'	Single Quote
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# \\	Backslash
txt = "This will insert one \\ (backslash)."
print(txt)

# \n	New Line
txt = "Hello\nWorld!"
print(txt)

# \r	Carriage Return
txt = "Hello\rWorld!"
print(txt) # this will print World! because the carriage return will move the cursor to the beginning of the line and overwrite the previous characters

# \t	Tab
txt = "Hello\tWorld!"
print(txt) # this will print Hello    World! because the tab will insert a tab space between the two words

# \b	Backspace
txt = "Hello\bWorld!"
print(txt) # this will print HelloWorld! because the backspace will remove the space between the two words

# \f	Form Feed
txt = "Hello\fWorld!"
print(txt) # this will print HelloWorld! because the form feed will insert a form feed between the two words

