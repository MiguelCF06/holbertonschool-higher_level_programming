#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        res = 0
        x = 0
        while x < len(roman_string):
            simb1 = valueRoman(roman_string[x])
            if x + 1 < len(roman_string):
                simb2 = valueRoman(roman_string[x + 1])
                if simb1 >= simb2:
                    res = res + simb1
                    x = x + 1
                else:
                    res = res + simb2 - simb1
                    x = x + 2
            else:
                res = res + simb1
                x = x + 1
        return res
    return 0
def valueRoman(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1
