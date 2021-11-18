#!/usr/bin/python3
import sys

def main(*argv):

    l = len(sys.argv)
    sum = 0
    if l > 1:
        for arg in sys.argv:
            if arg != sys.argv[0]:
                sum = sum + int(arg)

    print(sum)
if __name__ == "__main__":
    main()
