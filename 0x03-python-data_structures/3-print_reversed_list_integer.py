def print_reversed_list_integer(my_list=[]):
    lengthValue = len(my_list) - 1

    while lengthValue >= 0:
        print("{:d}".format(my_list[lengthValue]))
        lengthValue -= 1
