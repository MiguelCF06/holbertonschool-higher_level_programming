#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_copy = my_list[:]
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    elif idx > 0 and idx < len(my_list):
        del my_copy[idx]
    return my_copy
