#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    try:
        for iterator in range(x):
            print("{}".format(my_list[iterator]), end="")
            cont += 1
    except:
        return (cont)
    else:
        return (cont)
    finally:
        print("\n", end="")
