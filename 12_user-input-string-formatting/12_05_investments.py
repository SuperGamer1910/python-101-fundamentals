# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment_amount = input("What is the investment amount: ")
investment_amount = int(investment_amount)
interest_rate = input("What is the interest rate (in %): ")
interest_rate = int(interest_rate)
years_to_invest = input('For how many years do you want to invest the money: ')
years_to_invest = int(years_to_invest)

for i in range(1, years_to_invest + 1):
    interest_amount = investment_amount * interest_rate /100
    investment_amount = investment_amount + interest_amount
    print(f"Year {i} : {investment_amount}")