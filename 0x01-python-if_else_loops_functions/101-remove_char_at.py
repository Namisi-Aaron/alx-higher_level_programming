#!/usr/bin/python3
def remove_char_at(str, n):
    for char in range(len(str)):
            if char != n:
                print('{}'.format(str[char]), end='')
