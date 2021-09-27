#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
            print("{}".format(my_list[x]), end='')
            x + 1
    except (IndexError, TypeError):
        print("\n")
    return size(x) - 1
