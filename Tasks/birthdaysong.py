#!/usr/bin/python3

# Composing a birthday song for someone

def happy():
    print("Happy birthday to you")

def song(person):
    person = str(person)
    happy()
    happy()
    print("Happy birthday, dear {}".format(person) + ".")
    happy()
    print()

def main():
    person = input("Enter in your first name: ")
    song(person)

main()
