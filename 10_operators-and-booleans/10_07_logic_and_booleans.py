# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

two_plus_two = 2+2 
six_minus_two = 6-2

if two_plus_two and six_minus_two == 4:
    print("Both equations are equal to 4")
else:
    print("Anyone or Neither of the equations are equal to 4")

three_multiply_three = 3*2
twelve_minus_7 = 12-7

if three_multiply_three == 9 or twelve_minus_7 == 9:
    print("Both or anyone of the equations are equal to 9")
else:
    print("Neither of the equations are equal to 9")

sheep_color = "white"
cow_color = "white"

print(sheep_color is cow_color)