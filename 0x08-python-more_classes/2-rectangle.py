#!/usr/bin/python3
'''define a rectangle'''


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """return width"""
        return self.__width

    @property
    def height(self):
        """return height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate the area"""
        return self.width * self.height

    def perimeter(self):
        """calculate the perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2*self.height + 2*self.width)
