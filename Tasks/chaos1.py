#!/usr/bin/python3

# File: Chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates chaotic behavior.")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("Enter number of time you want the  number to appeaar: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)


main()
