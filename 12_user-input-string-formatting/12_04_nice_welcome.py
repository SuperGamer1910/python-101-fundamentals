# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input('What is your name?: ')
name = str(name)
first_name = name.split()[0]
print(f"Hello {first_name}, Nice to meet you")