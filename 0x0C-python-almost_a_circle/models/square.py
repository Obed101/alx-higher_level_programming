#!/usr/bin/python3
"""this module prints a square"""


from rectangle import Rectangle


class Square(Rectangle):
    """a square that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size => width attribute"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the new value to the size attribute"""
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates the instance attributes in particular order"""
        i = 0
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for attr in attributes:
                if i > len(args) - 1:
                    break
                setattr(self, attr, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dict form of the Square instance"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.__x,
                'y': self.__y
                }

    def __str__(self):
        """returns the string representation of the instance"""
        fh = '[Square] ({:d}) {:d}/{:d}'.format(self.id, self.__x, self.__y)
        sh = ' - {:d}'.format(self.__width)
        return fh + sh
