#!/usr/bin/python3
""" module that contains to_json_string function """
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON
    representation of an object (string):
    """
    data = json.dumps(my_obj)
    return data
