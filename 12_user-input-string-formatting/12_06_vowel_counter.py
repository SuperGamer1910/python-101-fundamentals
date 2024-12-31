# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

random_sentence= input('Type in a random sentence: ')
random_sentence = str(random_sentence)
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for c in random_sentence:
    if c == "a":
        count_a = count_a + 1
    elif c == "e":
        count_e = count_e + 1
    elif c == "i":
        count_i = count_i + 1
    elif c == "o":
        count_o = count_o + 1
    elif c == "u":
        count_u = count_u + 1

print(f"count of a: {count_a}")
print(f"count of e: {count_e}")
print(f"count of i: {count_i}")
print(f"count of o: {count_o}")
print(f"count of u: {count_u}")