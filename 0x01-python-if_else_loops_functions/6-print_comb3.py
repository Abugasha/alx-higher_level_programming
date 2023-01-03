#!/usr/bin/python3
for units in range(0, 9):
    for decs in range(units + 1, 10):
        if (units != 8 or decs != 9):
            print("{:d}{:d}".format(units, decs), end=", ")
print(units, end="")
print(decs)
