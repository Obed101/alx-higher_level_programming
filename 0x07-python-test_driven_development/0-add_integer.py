#!/usr/bin/python3
"""This Module adds two integers."""


def add_integer(a, b=98):
    """This function adds two integers
    tests:
    >>> add_integer(10, 5)
    15
    >>> add_integer(10.0, 5.1)
    15
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        elif type(b) is float:
            b = int(b)
    return int(a) + int(b)
