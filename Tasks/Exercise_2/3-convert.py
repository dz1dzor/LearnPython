#!/usr/bin/python3
print("Computes and prints a table of Celcius temperature and the ", end="")
print("Fahrenheit equivalents of every 10 degrees from 0 to 100")
for i in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
    fahrenheit = 9/5 * i + 32
    print(i, fahrenheit)
