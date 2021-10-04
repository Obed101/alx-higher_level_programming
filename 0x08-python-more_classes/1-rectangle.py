#!/usr/bin/python3
"""This module prints a rectangle"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ initializes the 'width' and 'height' attributes """

        self.__height = height
        self.__width = width
	@property
    def height(self):
        """Height getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height setter function"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """retrieves the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets value to the width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
