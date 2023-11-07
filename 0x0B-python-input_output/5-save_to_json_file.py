#!/usr/bin/python3

"""AUTOHR: MAHMOUD ABDEL MALEK """


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(to_json_string(my_obj))
