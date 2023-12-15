#!/usr/bin/python3

# Returning values

def add(num1, num2):
    result = num1 + num2
    return result

def main():
    print("Adding two numbers.\n")
    n1 = input("Enter in your first number: ")
    n2 = input("Enter in your second number: ")
    n1, n2 = int(n1), int(n2)
    total = add(n1, n2)
    print("The number you get when you add the two numbers", end="")
    print(" is {:d}".format(total))

main()
