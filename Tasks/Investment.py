#!/usr/bin/python3
print("This program calculates the future value of a 10-year investment.")
amount = eval(input("The principal amount is: "))
rate = eval(input("The interest rate in decimals: "))
for i in range(10):
    amount = amount * (1 + rate)
print("Your total investment after 10 years will be ", amount)
