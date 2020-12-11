#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_argv = len(argv) - 1
    if number_argv == 0:
        print("{} arguments.".format(number_argv))
    elif number_argv == 1:
        print("{} argument:".format(number_argv))
    else:
        print("{} arguments:".format(number_argv))
    if number_argv > 0:
        for i in range(1, number_argv + 1):
            print("{:d}: {:s}".format(i, argv[i]))
