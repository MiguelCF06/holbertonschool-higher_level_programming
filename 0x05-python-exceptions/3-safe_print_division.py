#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside Result: {}".format(res))
    return res
