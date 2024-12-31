# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

random_number= input('Type a random number to check if its divisible by 3: ')
random_number = int(random_number)

if random_number % 3 == 0:
    print("The number u entered is divisible by 3.")
else:
    print('This number is not divisible by 3')