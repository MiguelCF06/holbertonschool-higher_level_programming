#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copy = my_list[:]
    if idx < 0:
        return my_copy
    elif idx > len(my_list):
        return my_copy
    elif idx >= 0 and idx <= len(my_list):
        x = 0
        while my_copy[x] <= idx + 1:
            if my_copy[x] == idx + 1:
                my_copy[x] = element
                return my_copy
            x = x + 1
