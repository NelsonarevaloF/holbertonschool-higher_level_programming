#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = sorted(a_dictionary.items())
    for k in b_dictionary:
        print("{:s}: {}".format(k[0], k[1]))
