#!/usr/bin/python3
for i in range(10):
    j = i
    while j < 10:
        if i != j and (j != 9 or i != 8):
            print("{}{}, ".format(i, j), end='')
        j += 1
print("89")
