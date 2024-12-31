# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
random_number = random.randint(1,10)
i = 0
while i < 3 :
    guess = input('Guess the number between 1-10 within 3 tries: ')
    guess = int(guess)
    if guess != random_number:
        print("Woops! Wrong Guess")
    elif guess == random_number:
        print("Congratulations!! You guessed the correct number")
        break
    
    i = i + 1
    if i == 3:
        print(f"The correct number was: {random_number}")
