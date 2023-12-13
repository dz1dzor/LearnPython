#!/usr/bin/python3

# Simple string processiong program to generate usernames

def main():
    print("Generating your username\n")
    f_name = input("Enter in your first name(all lowercases): ")
    last_name = input("Enter in your last name(all lowercases): ")
    username = f_name[0] + last_name[:7]

    print("Your username is: ", username)

main()


