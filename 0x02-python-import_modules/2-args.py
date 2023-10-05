#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1, ))

    for i in range(len(sys.argv) - 1):
        print("{}: {}".format(i + 1, sys.argv[i+1]))
