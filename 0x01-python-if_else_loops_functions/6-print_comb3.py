#!/usr/bin/python3
for number1 in range(10):
    for number2 in range(10):
        if number1 < number2:
            print('{}{}'.format(number1, number2), end='')
            if number1 < 8:
                print(', ', end='')
print('\n', end='')
