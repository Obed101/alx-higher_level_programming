#!/usr/bin/python3
"""Rectangle module for all rectangle tasks"""

from base import Base


class Rectangle(Base):
    """A rectangle class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance initializer"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = int(x)
        self.__y = int(y)

    @property
    def width(self):
        """calculates the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value to the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value to the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets value to the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of the Rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """prints the attributes in a string format"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def display(self):
        """prints the rectangle instance with the # character"""
        buffer = [' ' * self.x + '#' * self.width for _ in range(self.height)]
        print('\n' * self.y + '\n'.join(buffer))

    def update(self, *args, **kwargs):
        """assigns argument to each attribute in particular order"""
        i = 0
        attributes = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for attr in attributes:
                if i == len(args):
                    break
                setattr(self, attr, args[i])
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """representaion in dict form"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
