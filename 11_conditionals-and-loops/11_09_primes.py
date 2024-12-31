# Print out every prime number between 1 and 1000.

for i in range(2, 1000):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count = count + 1
    if count == 0:
        print(i)