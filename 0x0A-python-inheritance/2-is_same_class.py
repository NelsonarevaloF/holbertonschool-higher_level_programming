#!/usr/bin/python3
"""in this module is the function is_same_class"""


def is_same_class(obj, a_class):
    """
    this function return true if obj is type a_class
    othewise return 0
    """
    return type(obj) == a_class
