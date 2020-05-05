#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    my_copy = my_list[:]
    my_copy.reverse()
    if my_copy:
        for x in range(len(my_copy)):
            print("{}".format(my_copy[x]))
