# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number


number= 60

if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
elif number % 3 == 0:
        print("Fizz")
elif number % 5 == 0:
        print("Buzz")