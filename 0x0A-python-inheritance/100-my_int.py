#!/usr/bin/python3
"""This module inverts comparison operators"""


class MyInt(int):
    """This class creates a personalized int"""

    def __eq__(self, other):
        """handles the == operator"""
        return True if self != other else False
    
    def __ne__(self, other):
        return True if self != other else False
