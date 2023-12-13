#!/usr/bin/python3
print("Calculates the future value of an investment for a number ", end="")
print("of years when you continue to deposit a fixed amount every year.")
year = eval(input("The number of years to invest: "))
fixed_amount = eval(input("The principal amount is: "))
rate = eval(input("The interest rate in decimals: "))
amount = fixed_amount
for i in range(year):
    amount = amount * (1 + rate)
    # TODO: I have to work on this to prevent adding the fixed amount exactly
    # before printing the final answer
    # amount = amount + fixed_amount
print("Your total investment after", year, " years will be ", amount)
