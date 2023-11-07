#!/usr/bin/python3
import json
"""AUTOHR: MAHMOUD ABDEL MALEK """


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
         represented by a JSON string
    """
    return json.loads(my_str)
