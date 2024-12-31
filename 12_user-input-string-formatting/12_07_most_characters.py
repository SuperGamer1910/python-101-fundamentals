# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

first_strings = input("Write down ur 1st word: ")
second_strings = input("Write down ur 2nd word: ")
third_strings = input("Write down ur 3rd word: ")

first_string_len = len(first_strings)
second_string_len = len(second_strings)
third_string_len = len(third_strings)

if first_string_len > second_string_len and first_string_len > third_string_len:
    print(first_strings, first_string_len)
elif second_string_len > first_string_len and second_string_len > third_string_len:
    print(second_strings, second_string_len)
elif third_string_len > first_string_len and third_string_len > second_string_len:
    print(third_strings, third_string_len)