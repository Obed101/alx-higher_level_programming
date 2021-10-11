#!/usr/bin/python3
"""Inheritance module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits features of Rectangle """

    def __init__(self, size):
        """ instantiation initializer """
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2
