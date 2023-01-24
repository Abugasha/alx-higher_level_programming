#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print_count = 0

    for index in range(0, x):
        try:
            print("{}".format(my_list[index]), end="")
            print_count += 1
        except IndexError:
            pass
        except ValueError:
            pass
    print()
    return(print_count)
