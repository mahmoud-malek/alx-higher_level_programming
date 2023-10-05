#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as clc

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, clc.add(a, b)))
    print("{} - {} = {}".format(a, b, clc.sub(a, b)))
    print("{} * {} = {}".format(a, b, clc.mul(a, b)))
    print("{} / {} = {}".format(a, b, clc.div(a, b)))
