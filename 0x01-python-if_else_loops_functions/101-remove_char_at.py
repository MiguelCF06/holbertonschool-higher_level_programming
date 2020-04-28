#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ''
    j = 0
    for x in str:
        if j != n:
            strcpy = strcpy + x
        j = j + 1
    return strcpy
