#!/usr/bin/python3
"""Detect instance deletion"""


class Rectangle:
    """class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        '''destructor'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def __str__(self):
        """return a string with the rectangule in # characters"""
        return_str = ""
        if self.width == 0 or self.height == 0:
            return return_str
        for a in range(self.height):
            for b in range(self.width):
                return_str += str(self.print_symbol)
            if a != (self.height - 1):
                return_str += "\n"
        return return_str

    def __repr__(self):
        """return a string with the rectangule in # characters"""
        return self.__class__.__name__ + str((self.width, self.height))
