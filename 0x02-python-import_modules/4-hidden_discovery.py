#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    strings = dir(hidden_4)
    for string in strings:
        if not string.startswith("__"):
            print(string)
