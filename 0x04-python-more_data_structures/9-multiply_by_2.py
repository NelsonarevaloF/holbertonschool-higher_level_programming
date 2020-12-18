#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for elem in b_dictionary:
        b_dictionary[elem] = b_dictionary.get(elem) * 2
    return b_dictionary
