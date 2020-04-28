#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha in [101, 113]:
        continue
    else:
        print(chr(alpha), end='')
