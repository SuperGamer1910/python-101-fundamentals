# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

birth_month = input("Write down the number of your Birth date: ")
birth_month = int(birth_month)
if birth_month > 0:
    if birth_month > 1:
        if birth_month > 2:
            if birth_month > 3:
                if birth_month > 4:
                    if birth_month > 5:
                        if birth_month > 6:
                            if birth_month > 7:
                                if birth_month > 8:
                                    if birth_month > 9:
                                        if birth_month > 10:
                                            if birth_month > 11:
                                                if birth_month > 12:
                                                    print('Number out of range')
                                                else:
                                                    print("Your Birthday is in December!!")
                                            else:
                                                print("Your Birthday is in November!!")
                                        else:
                                            print("Your Birthday is in October!!")
                                    else:
                                        print("Your Birthday is in September!!")
                                else:
                                    print("Your Birthday is in August!!")
                            else:
                                print("Your Birthday is in July!!")
                        else:
                            print("Your Birthday is in June!!")
                    else:
                        print("Your Birthday is in May!!")
                else:
                    print("Your Birthday is in April!!")
            else:
                print("Your Birthday is in March!!")
        else: 
            print("Your Birthday is in February!!")
    else:
        print("Your Birthday is in January!!") 
else:
    print("Number out of range")              
                            