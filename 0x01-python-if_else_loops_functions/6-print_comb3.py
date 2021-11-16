#!/usr/bin/python3
for x in range(10):
    for k in range((x+1), 10):
        if (x != 8 or k != 9):
            print("{}{}, ".format(x, k), end="")

        else:
            print("{}{}".format(x, k))
