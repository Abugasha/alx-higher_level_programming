#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    denominator = 0
    if not my_list:
        return (0)
    for i in range(0, len(my_list)):
        numerator = my_list[i][0] * my_list[i][1] + numerator
    for i in range(0, len(my_list)):
        denominator = my_list[i][1] + denominator
    return(numerator/denominator)

