#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_int = my_list[0]
    for integer in my_list:
        if integer >= max_int:
            max_int = integer
        else:
            continue
    return max_int
