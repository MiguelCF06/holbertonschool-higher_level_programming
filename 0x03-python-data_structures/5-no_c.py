#!/usr/bin/python3
def no_c(my_string):
    mycpy = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            mycpy = mycpy + x
    return mycpy
