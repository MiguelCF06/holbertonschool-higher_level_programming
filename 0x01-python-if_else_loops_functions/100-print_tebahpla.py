#!/usr/bin/python3
for alpha in reversed(range(97, 123)):
        if (alpha % 2):
                print(str.upper(chr(alpha)), end='')
        else:
                print('{}'.format(chr(alpha)), end='')
