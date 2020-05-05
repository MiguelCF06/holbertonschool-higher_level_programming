#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_copy = my_list.copy()
    lar = len(my_copy)
    for x in range(0, lar):
        if my_list[x] % 2 == 0:
            my_copy[x] = True
        else:
            my_copy[x] = False
    return my_copy
