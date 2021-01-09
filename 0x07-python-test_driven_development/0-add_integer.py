#!/usr/bin/python3
""" here is the add integer function """


def add_integer(a, b=98):
    """ this function add two integer numbers """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
