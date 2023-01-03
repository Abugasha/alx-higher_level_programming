#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (ord(str[i]) < 97 or ord(str[i]) > 122):
            upper_character = str[i]
        else:
            upper_character = chr(ord(str[i]) - 32)
        print("{}".format(upper_character), end="")
    print()
