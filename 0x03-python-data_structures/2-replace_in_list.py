#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    elif idx >= 0 and idx <= len(my_list):
        x = 0
        while my_list[x] <= idx + 1:
            if my_list[x] == idx + 1:
                my_list[x] = element
                return my_list
            x = x + 1
