#!/usr/bin/python3
# scopes1.py
# Local versus global

# we define a function called local
def local():
    m = 7
    print(m)


m = 5
print(m)

local()
