# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

answer = input('Is pineapples on pizza a good combination: ')

result = ""

for i in range(len(answer)):
    if i % 2 == 0:
       result = result + answer[i].lower()
    else:
        result = result + answer[i].upper()
    print(f"stage {i}, result: {result}")
print(result)