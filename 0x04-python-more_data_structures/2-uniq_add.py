#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    acum = 0
    for x in a:
        acum += x
    return acum
