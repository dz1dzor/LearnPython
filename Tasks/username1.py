#!/usr/bin/python3

# Creating usernames for students in a school

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print("Creating usernames for students in a school")

# inputFileName = input("The file name where the names of the student is: ")
    inputFileName = askopenfilename()
# outputFileName = input("The name of the file to store the usernames: ")
    outputFileName = asksaveasfilename()

    inFile = open(inputFileName, "r")
    outFile = open(outputFileName, "w")

    for line in inFile:
        firstname, lastname = line.split()
        username = (firstname[0] + lastname[:7]).lower()
        print(username, file=outFile)

    inFile.close()
    outFile.close()

    print("\nFile created")

main()
