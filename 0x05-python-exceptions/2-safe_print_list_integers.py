#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    for i in range(0, x):
        if isinstance(my_list[i], int):
            try:
                print('{:d}'.format(my_list[i]), end='')
                integers_printed += 1
            except Exception as e:
                print(e)
        else:
            continue
    print('\n', end='')
    return integers_printed
