#!/usr/bin/python3

""" This is a program to add all its arguments, Made by: mahmoud malek """

if __name__ == "__main__":

    import sys
    total = 0
    for i in sys.argv[1:]:
        total += int(i)
    print(total)
