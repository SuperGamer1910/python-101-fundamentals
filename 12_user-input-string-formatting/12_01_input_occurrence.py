# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

sentence = input("Write a random sentence: ")
letter = input('Type in the letter you want to find: ')
sentence = str(sentence)
result = sentence.find(letter)
print(result)