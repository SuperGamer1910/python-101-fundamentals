# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

#egg
#flour
#butter
#apple

apple = s[7:12]
print(apple)

flour = s[-9:-4]
print(flour)

butter = s[-20:-14]
print(butter)

egg = s[26:29]
print(egg)