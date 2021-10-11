#!/usr/bin/python3
"""Inheritance module"""

import 7-base_geometry
class Rectangle(BaseGeometry):
    """Defines a rectangle"""
    def __init__(self, width, height):
        self.__width = int(width)
        self.__height = int(height)
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(width) != int:
            raise TypeError("width must be an integer")
