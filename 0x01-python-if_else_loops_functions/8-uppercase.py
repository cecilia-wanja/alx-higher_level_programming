#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if i >= 65 and i <= 90:
            print("{:c}".format(i), end="")
    print("")
