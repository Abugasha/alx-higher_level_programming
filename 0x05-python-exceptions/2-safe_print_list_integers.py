#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_count = 0

    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            print_count += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return(print_count)
