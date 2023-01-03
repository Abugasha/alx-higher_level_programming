#!/usr/bin/python3
def remove_char_at(str, n):
    copy = [None] * len(str)
    result = ""
    if (n <= len(str) and n >= 0):
        copy[0:n] = str[0:n]
        copy[n + 1:len(str)] = str[n + 1:len(str)]
        copy = list(filter(None, copy))
        for ele in copy:
            result += ele
    else:
        result = str
    return(result)
