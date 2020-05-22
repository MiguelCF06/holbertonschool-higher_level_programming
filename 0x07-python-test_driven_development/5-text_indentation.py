#!/usr/bin/python3
"""
Print a text with new lines when
encounter "." ":" or "?"
"""


def text_indentation(text):
    """
    Function with one argument: (text)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        f = 0
        for letter in text:
            if f == 0:
                if letter == " ":
                    continue
                else:
                    f = 1
            if f == 1:
                if letter == "." or letter == "?" or letter == ":":
                    print(letter)
                    print()
                    f = 0
                else:
                    print(letter, end="")
