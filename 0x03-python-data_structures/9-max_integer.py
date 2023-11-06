#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    if len(my_list) == 0:
        return None
    for integer in my_list:
        if integer > max_int:
            max_int = integer
        else:
            continue
    return max_int
