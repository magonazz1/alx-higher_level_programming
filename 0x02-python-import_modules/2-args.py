#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1

    if (argc == 0):
        print("0 arguments.")

    elif (argc == 1):
        print("1 argument:")

    else:
        print("{} arguments:".format(argc))

    for a in range(argc):
        print("{}: {}".format(a + 1, sys.argv[a + 1]))
