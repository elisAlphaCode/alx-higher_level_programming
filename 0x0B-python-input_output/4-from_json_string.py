#!/usr/bin/python3
""" module that contains from_json_string function """
import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string:
    """
    data = json.loads(my_str)
    return data
