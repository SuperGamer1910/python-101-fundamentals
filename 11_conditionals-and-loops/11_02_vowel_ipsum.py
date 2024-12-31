# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

vowel_a = lorem_ipsum.count("a")
vowel_e = lorem_ipsum.count("e")
vowel_i = lorem_ipsum.count("i")
vowel_o = lorem_ipsum.count("o")
vowel_u = lorem_ipsum.count("u")

total_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
print(f"There are {total_vowels} vowels in this text")