#!/usr/bin/python3
def roman_to_int(roman_string):
    value = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    if type(roman_string) == str:
        prev = 0
        res = 0
        n = len(roman_string)
        for x in range(n-1, -1, -1):
            if value[roman_string[x]] >= prev:
                res += value[roman_string[x]]
            else:
                res -= value[roman_string[x]]
            prev = value[roman_string[x]]
        return res
    return 0
