# Operators
# Operators are used to perform  operations on variables and values.
#Python  divides them in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arthmetic operators
# Are used with numeric values to perform mathematical operations

x= 5
y = 4

print(x + y) # this is the addtiotion operator, it will return 9
print(x - y) # this the subratction operator, it will return 1
print(x * y) # this is the multiplication operator it will return 20
print(x / y) # this is the division operator it will return 1.25
print(x % y) # this is the modulus operator it will return 1  because 5 divided by 4 leaves a reminder of 1
print(x ** y) # this is the exponential operator it will return 625 because 5 to the power of 4 is 625
print(x // 4) # this is the floor division operator it will return 1 because 5 divided by 4 is 1.25 but floor division will rouund down to the nearest whole number.


# Assignment operators
# Arte used to assign values to a variable

x = 5 # this is the simple assignment operator it will asssign the value 5 to the variable x
print(x)

x += 3  # this is the add and assignment operator it will add 3 to the current value of x and assign the result back to x, so x will now be 8
# same as  x = x + 3
print(x)

x -= 2 # this is the subtract and assignment operator it will subtract 2 from the current value of x and assign the result back to x, so x will now be 6
# same as x = x - 2
print(x)

x *= 2 # this is the multipy and assignment operator it willmultiply the current value of x by 2 and assign the result back to x, so x will be 12
# same as x = x * 2
print(x)

x /= 4 # this is the division and assignment operator it will divide the current value of x by 4 and assign the result back to x, so x will now be 2
# same as x = x / 4
print(x)

x %= 3 # this is the modulus and the assignment operator it will divide the current value of x by 3 and assign the reminder back to x so x will be 2 because 2 divided by 3  leaves a reminder of 2
# same as x = x % 3
print(x)

x //= 2 # this is the floor division and assignment operator it will divide the current value  of x by 2 and assign the result back to x so x will be 1 because 2 divided by 2 is 1 and floor divison will round down to the nearest whole number
# same as x = x // 2
print(x)

x **= 3 # this is the exponential and assignment operator it will raise the current value of x to the power of 3 and assign the value back to x so x will be 1 because 1 to the power of 3 is 1
# same as x = x ** 3
print(x)

x &= 2 # this is the bitwise and assignment operator it will perform a bitwise and operation on the current value of x and 2 and assign the value back to x so x will be 0 because the bitwise and of 1 and 2 is 0
# same as x = x & 2
print(x)

x |= 2 # this is the bitwise or assignment operator it will perform a bitwise or operaton on the current value of x and 2 and asign the value back to x so x will be 2 because the bitwise or of 0 and 2 is 2
# same as x = x | 2
print(x)

x ^= 2 # this is the bitwise exclusive or assignment operator it will perform a bitwise exclusive or operation on the current value of x and 2 and assign the value back to x so x will be 0 because the bitwise exclusive or of 2 and 2 is 0
# same as x = x ^ 2
print(x)

x >>= 2 # this is the right shift assignment operator it will perform a right shift operation on the current value of x by 2 bits and assign the value back to x so x will be 0 because right shifting 0 by any number of bits will always be 0
# same as x = x >> 2
print(x)

x <<= 2 # this is the left shift assignment operator it will perform a left shift operation on the current value of x by 2 bits  and assign the value back to x so x will be 0 because left shifting 0 by any number of bits will be 0
# same as x = x << 2 
print(x)

# this is the walrus operator := it will assign the value 5 to x and return the value. It assigns values to variables as part of a larger expression:
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3: # this will assign the length of the numbers list to the variable count and then check if count is greater than 3
    print(f"List has {count} elements") # this will print "List has 5 elements" because the length of the numbers list is 5 which is greater than 3
print(x)


# Comparision Operators
# Are use to compare two values and return a boolean value  based on the comparison

x = 5
y = 3

print(x == y) # this is the equal to operator it will return false because 5 is not equal to 3
print(x != y) # this is the not equal to opertaor it will return true because 5 is not equal to 3
print(x > y) # this is the greater than operator it will return true because  5 is grater than 3
print(x < y) # this is the less than opertaor it will return false because 5 is not less than 3
print(x >= y) # this is the greater than or equal to operator it will return true because 5 is greater than 3
print(x <= y) # this is the less than or equal to opertaor it will return flase because 3 is not less than or equal to 5

# chaining comparison operators python allows u to chain multiple comparison operators together in a single expression to compare multiple values at one
x = 5 
print(1 < x < 10) # this will return true because 1 is less than 5 and 5 is less than 10

print(1 < x and x < 10) # this will also return true because 1 is less than 5 and 5 is less than 10


# Logical operators
# Are use to combine conditional statements and return a boolean value based on the combination
x = 5 
print(x > 3 and x < 10) # this will return true because 5 is greater than 3 and 5 is less than 10. It always return true if both statements are true otherwise it will return false.
print(x > 3 or x < 4) # this will return true becauuse 5 is greater than 3. It will return true if at least one of the statements is true otherwise it will return false.
print(not(x > 3 and x < 10)) # this will return false because the expression inside the not operator is true and the not operator will return the opposite of that which is false

# Identity Operators
# Are used to compare objects not if ther are equal bu if actually they are the same object with the same memory location

x = ["apple", "banana", "Cherry"]
y = ["apple", "banana", "Cherry"]
z = x

print(x is y) # this will return false because x and y are two diffrent objects in memory even though they have the same content 
print(x is not y) # this will return true because x and y are two diffrent objects in memeory
print(x is z) # this will return true because x and z are the same object in memory
print(x is not z) # this will return false because x and z are the same object in memory
print(x == y) # this will return true because x and y have the same content even though they are diffrent objects in memory


# Membership Operators
# Are used to test if a sequence is presented in an object
x = ["apple", "bannana", "cherry"]

print("apple" in x) # this will return true because "apple" is in the list x
print("grape" in x) # this will return false because "grape" is not in the list x
print("banana" not in x) # this will return false because "banana" is in the list x
print("grape" not in x) # this will return true because "grape" is not in the list x


# Bitwise Operators
# are used to compare binary numbers and perform bitwise operations on them
x = 5 # in binary 0101
y = 3 # in binary 0011

# & this is the bit wise and operator it will compare each bit of the binary representation of x and y and return a new binary number
# where each bit is 1 if both bits are 1 otherwise it will be zero. 
# so 5 & 3 will return 1 because the bitwise and of 0101 and 0011 is 0001

print(x & y) # this will return 1

# | this is the bitwise or operator it will compare each bit of the binary representation of x and y and return a new binary number 
# where each bit is 1 if at least one of the bits is 1 otherwise it will be 0
# so 5 | 3 will return 7 because the bitwise or of 0101 and 0011 is 0111
print(x | y) # this will return 7

# ^ this is the bitwise exclusive or operator it will compare each bit of the binary representation of x and y and return a new binary number
# where each bit is 1 if the bits are different and 0 if they are the same
# so 5 ^ 3 will return 6 because the bitwise exclusive or of 0101 and 0011 is 0110
print(x ^ y) # this will return 6


# ~ this is the bitwise not operator it will return the complement of the binary representation of x
# so ~5 will return -6 because the bitwise not of 0101 is 1010 in two's complement representation which is -6 in decimal
print(~x) # this will return -6

# << this is the left shift operator it will shift the bits of x to the left by the number of positions specified by y and fill the rightmost bits with 0
# so 5 << 3 will return 10 because shifting the bits of 0101 to the left by 3 positions gives 10100 which is 10 in decimal
print(5 << 3) # this will return 10

# >> this is the right shift operator it will shift the bits of x to the right by the number of positions specified by y and fill the leftmost bits with 0
# so 5 >> 3 will return 2 because shifting the bits of 0101 to the right by 3 positions gives 0010 which is 2 in decimal
print(5 >> 3) # this will return 2


# Operator precedence
# Operator precedence determines the order in which operators are evaluated in an expression.BODMAS is the order of operator precedence in Python which stands for Brackets, Orders (exponents), Division and Multiplication, Addition and Subtraction. Operators with higher precedence are evaluated before operators with lower precedence. If two operators have the same precedence, they are evaluated from left to right.
x = 5 + 3 * 2 # this will return 11 because the multiplication operator has higher precedence than the addition operator so it will be evaluated first and then the addition operator will be evaluated
print(x)

# Parenthesis has the highest precedence so it will be evaluated first
x = (5 + 3) * 2 # this will return 16 because the expression inside the parenthesis will be evaluated first and then the multiplication operator will be evaluated
print(x)

# Exponents has higher precedence than multiplication and division so it will be evaluated first
x = 2 ** 3 * 4 # this will return 32 because the exponent operator has higher precedence than the multiplication operator so it will be evaluated first and then the multiplication operator will be evaluated
print(x)

# Unary plus, unary minus, and bitwise NOT have the same precedence and they are evaluated from right to left +x  -x  ~x so they will be evaluated before multiplication and division
x = -5 * 3 # this will return -15 because the unary minus operator has higher precedence than the multiplication operator so it will be evaluated first and then the multiplication operator will be evaluated
print(x)

# Unary plus, unary minus, and bitwise NOT has higher  precedence than multiplication and division so they will be evaluated first
x = -5 + 3 # this will return -2 because the unary minus operator has higher precedence than the addition operator so it will be evaluated first and then the addition operator will be evaluated
print(x)

# Multiplication has higher precedence than division so it will be evaluated first
x = 5 * 3 / 2 # this will return 7.5 because the multiplication operator has higher precedence than the division operator so it will be evaluated first and then the division operator will be evaluated
print(x)

# Division and multiplication has higher precedence than addition and subtraction so they will be evaluated first
x = 5 + 3 * 2 - 4 / 2 # this will return 9 because the multiplication and division operators have higher precedence than the addition and subtraction operators so they will be evaluated first and then the addition and subtraction operators will be evaluated from left to right
print(x)

# floor division, Modulus have the same precedence and they are evaluated from left to right so they will be evaluated before addition and subtraction
x = 10 + 5 // 2 - 3 % 2 # this will return 12 because the floor division and modulus operators have the same precedence and they are evaluated from left to right so 5 // 2 will be evaluated first and then 3 % 2 will be evaluated and then the addition and subtraction operators will be evaluated from left to right
print(x)

# Modulus, floor division, has higher precedence than addition and subtraction so they will be evaluated first
x = 10 % 3 + 5 // 2 - 1 << 2 # this will return 12 because the modulus, floor division, and bitwise shift operators have higher precedence than the addition and subtraction operators so they will be evaluated first and then the addition and subtraction operators will be evaluated from left to right
print(x)

# addition has higher precedence than subtraction so it will be evaluated first
x = 10 - 5 + 2 # this will return 7 because the addition operator has higher precedence than the subtraction operator so it will be evaluated first and then the subtraction operator will be evaluated
print(x)

# Subtraction has higher presidense that left shift and right shift so it will be evaluated first
x = 10 - 5 << 2 # this will return 20 because the subtraction  operator has higher precedence than the bitwise shift operator so it will be evaluated first and then the bitwise shift operator will be evaluated
print(x)

# Bitwise shift operators has same peseidence and are evaluatted from left to right
x = 10 << 2 >> 1 # this will return 20 because the bitwise shift operators have the same precedence and they are evaluated from left to right so 10 << 2 will be evaluated first and then the result will be right shifted by 1
print(x)

# Bitwise shift operators has higher precedence than bitwise and, bitwise or, and bitwise exclusive or so they will be evaluated first
x = 5 & 3 << 2 # this will return 1 because the bitwise shift operator has higher precedence than the bitwise and operator so it will be evaluated first and then the bitwise and operator will be evaluated
print(x)

# Bitwise and has higher precedence than bitwise exclusive or and bitwise or so it will be evaluated first
x = 5 & 3 ^ 2 # this will return 3 because the bitwise and operator has higher precedence than the bitwise exclusive or operator so it will be evaluated first and then the bitwise exclusive or operator will be evaluated
print(x)

# Bitwise exclusive or has higher precedence than bitwise or so it will be evaluated first
x = 5 ^ 3 | 2 # this will return 7 because the bitwise exclusive or operator has higher precedence than the bitwise or operator so it will be evaluated first and then the bitwise or operator will be evaluated
print(x)

# Bitwise or has a higher precedence than Comparisons, identity, and membership operators so it will be evaluated first
x = 5 | 3 > 2 # this will return true because the bitwise or operator has higher precedence than the comparison operator so it will be evaluated first and then the comparison operator will be evaluated
print(x)

# Comparison operators, identity operators, and membership operators have the same precedence and they are evaluated from left to right
x = 5 > 3 == True # this will return true because the comparison operators have the same precedence and they are evaluated from left to right so 5 > 3 will be evaluated first and then the result will be compared to True
print(x)

# comparison operators, identity operators, and membership operators have higher precidence than Logical NOT so they will be evaluated first
x = not 5 > 3 # this will return false because the comparison operator has higher precedence than the logical not operator so it will be evaluated first and then the logical not operator will be evaluated
print(x)

# Logical Not has higher precedence than Logical AND so it will be evaluated first
x = not True and False # this will return false because the logical not operator has higher precedence than the logical and operator so it will be evaluated first and then the logical and operator will be evaluated
print(x)

# Logical AND has higher precedence than Logical OR so it will be evaluated first
x = True or False and False # this will return true because the logical and operator has higher precedence than the logical or operator so it will be evaluated first and then the logical or operator will be evaluated
print(x)


