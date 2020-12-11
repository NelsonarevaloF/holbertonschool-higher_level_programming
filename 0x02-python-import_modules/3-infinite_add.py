#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_argv = len(argv) - 1
    if number_argv == 0:
        print(0)
    elif number_argv == 1:
        print("{:d}".format(int(argv[1])))
    else:
        accum = 0
        for i in range(1, number_argv + 1):
            accum += int(argv[i])
        print("{:d}".format(accum))
