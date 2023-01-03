#!/usr/bin/python3
for i in range(0, 26):
    if (97 + i != 113 and 97 + i != 101):
        print("{:s}".format(chr(97 + i)), end="")
