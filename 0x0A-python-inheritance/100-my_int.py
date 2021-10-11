#!/usr/bin/python3
"""This module inverts comparison operators"""


class MyInt(int):
    """This class creates a personalized int"""

    def __init__(self, num):
        """initializes the class"""
        self.num = num

    def __eq__(self, other):
        """handles the == operator"""
        if self.num != other:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num < 0:
            return True if self.num != other else False
        if self.num == other:
            return True
        return False
