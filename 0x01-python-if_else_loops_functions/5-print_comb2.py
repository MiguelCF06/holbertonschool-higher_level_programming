#!/usr/bin/python3
for numbers in range(100):
    if numbers <= 98:
        print('{0:0=2d}, '.format(numbers), end='')
    elif numbers in [99]:
        print('{}'.format(numbers))
