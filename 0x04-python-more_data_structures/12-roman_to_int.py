#!/usr/bin/python3
def roman_to_int(roman_string):

    acumulator = 0
    if not roman_string or type(roman_string) is not str:
        return acumulator
    r_dict = {
                'M': 1000,
                'D': 500,
                'C': 100,
                'L': 50,
                'X': 10,
                'V': 5,
                'I': 1
    }
    for i in range(0, len(roman_string)):
        try:
            if (r_dict[roman_string[i]] >= r_dict[roman_string[i + 1]]):
                acumulator = r_dict[roman_string[i]] + acumulator
            else:
                acumulator = - r_dict[roman_string[i]] + acumulator
        except IndexError:
            acumulator = r_dict[roman_string[i]] + acumulator
    return(acumulator)

