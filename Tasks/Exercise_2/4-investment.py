#!/usr/bin/python3
print("Calculates the future value of an investment for a number of years.")
year = eval(input("The number of years to invest: "))
amount = eval(input("The principal amount is: "))
rate = eval(input("The interest rate in decimals: "))
for i in range(year):
    amount = amount * (1 + rate)
print("Your total investment after", year, " years will be ", amount)
