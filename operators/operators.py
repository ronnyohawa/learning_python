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

