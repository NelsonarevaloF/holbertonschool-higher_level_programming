#!/usr/bin/python3
"""defines a square"""


class Square:
    """this class initialize the size attribute"""
    def __init__(self, size=0):
        """this method initialize the size attribute"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """this method return the square"""
        return self.__size * self.__size