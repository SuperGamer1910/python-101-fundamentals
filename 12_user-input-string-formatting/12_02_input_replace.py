# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

sentence = input("Write down 3 sentences:")
sentence = str(sentence)
print(sentence[0])

result = sentence.replace(sentence[0],"#")
print(result)