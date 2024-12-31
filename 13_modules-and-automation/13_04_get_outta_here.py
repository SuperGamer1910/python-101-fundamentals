# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.asf
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys


while True:
    word = input("Guess the word: ")
    if word == "quit":
        sys.exit()