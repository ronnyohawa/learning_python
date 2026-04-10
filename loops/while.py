# While Loop
# With while Loop we can execute a set of statements as long as a condition is true
# print i as long as i is less than 6
# this loop requires relevant variables to be ready so here we define a variable i with  value of 1
i = 1

while i < 6:
    print(i)
    i += 1 # we increment i or the loop will run forever

# The break statement
# We can stope the loop  even if the loop condition is true
i = 1
while i < 8:
    print(i)
    if i == 3:
        break
    i += 1

# Continue statement
# We can stop the current iteraion and continue with the next
i = 0
while i < 8:
    i += 1
    if i == 3:
        continue
    print(i)

# Else styatement
# we can run a block of code once the condition no longer true
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
i = 1

while i < 6:
    print(i)
    i += 1
else:
    print("I is no longer less than 6")
