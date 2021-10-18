#!/usr/bin/python3
"""This is the module containing the base class"""


class Base:
    """this is the base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instance initializer"""
        self.id = id
        if self.id is not None:
            self.id = int(self.id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
