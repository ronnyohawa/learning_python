# MATCH STATEMENT
# Is used to perform  diffrent actions based on diffrent conditions
# Instead  of writing many if else statements  we can use the match statement
# It selects one of many blocks  to be executed

"""match expression: = This is evaluated once
  case x:
    code block
  case y:
    code block
  case z:
    code block """

day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tue")
    case 3:
        print("Wen")
    case 4:
        print("thur")

# Default value we use the  underscorse _ as the last case 
    case _:
        print("Looking foward")

# Combining values using thepipe character | as ana operator in the case  evaluation  to check  for more  than one  value in one case :
day = 2

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("This are week days")
    case 6 | 7:
        print("This are week ends")

# using if as a gaurd
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print(" A weekday in april")
    case 1|2|3|4|5 if month == 5:
        print("A week day in may")
    case _:
        print("No day or month")
