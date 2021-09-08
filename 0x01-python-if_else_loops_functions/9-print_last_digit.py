#!/usr/bin/python3
def print_last_digit(number):
    """Returns the last digit of a number."""
    if number < 0:
        number = number % 10
        return number
