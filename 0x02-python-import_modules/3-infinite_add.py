#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args_n = 0

    for a in range(len(sys.argv) - 1):
        args_n = args_n + int(sys.argv[a + 1])

    print("{}".format(args_n))
