#!/usr/bin/python3
# Dealing with factorial of a number
print("Program that computes the factorial of 10")
n = int(input("The number you want to compute the factorial of: "))
fact = 1
for factor in range(1, n+1):
    fact = fact * factor
print(fact)
