#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length_value = len(my_list) - 1

    while length_value >= 0:
        print("{:d}".format(my_list[length_value]))
        length_value -= 1
