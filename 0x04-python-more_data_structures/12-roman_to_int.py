#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i, res = 0, 0
    while i < len(roman_string) - 1:
        a, b = romans.get(roman_string[i]), romans.get(roman_string[i + 1])
        if (a < b):
            res += b - a
            i += 2
        else:
            res += a
            i += 1
    if i < len(roman_string):
        res += romans.get(roman_string[i])
    return res
