#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for chara in my_string:
        if chara == 'c' or chara == 'C':
            continue
        else:
            new_str += chara
    return new_str
