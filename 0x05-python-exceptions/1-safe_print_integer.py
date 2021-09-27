#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{d}".format(value), end='')
    except typeError:
            print("\n")
    return True if value else False
