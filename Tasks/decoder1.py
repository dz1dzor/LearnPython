#!/usr/bin/python3

# Decodes an encoded message

def main():
    print("Decodes an encoded message.\n")
    enc = input("The encoded message: ")
    msg = ""
    for num in enc.split():
        tmp = chr(int(num))
        msg = msg + tmp

    print(msg)

main()
