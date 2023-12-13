#!/usr/bin/python3

# Encoding the message inputted by a user

def main():
    print("Encoding messages.\n")
    msg = input("Enter your message: ")
    print("The encoded form is: ")
    for ch in msg:
        print(ord(ch), end=" ")

    print()

main()
    
