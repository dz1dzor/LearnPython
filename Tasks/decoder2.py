#!/usr/bin/python3

# Decodes an encoded message
# Efficient one

def main():
    print("Decodes an encoded message.\n")
    enc = input("The encoded message: ")
    char = []
    for num in enc.split():
        tmp = int(num)
        char.append(chr(tmp))

    msg = "".join(char)

    print(msg)

main()
