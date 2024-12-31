# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = input("Type in a random number: ")
number = int(number)
i = 0
while i < 1000000000:
    i = i + 1
    print(i)
    if i == number:
        
        print('Number Found.')
        break 