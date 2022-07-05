#!/usr/bin/python3
""" module that contains append_write module """


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a
    file (UTF8) and returns the number of characters added:
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
