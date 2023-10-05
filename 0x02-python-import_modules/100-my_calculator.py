#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as clc
    import sys

    size = len(sys.argv)
    if (size != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    operators = {"+": clc.add, "-": clc.sub, "/": clc.div, "*": clc.mul}

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))
