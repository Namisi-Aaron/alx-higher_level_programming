#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number_printed = 0
    for i in range(0, x):
        try:
            print('{}'.format(my_list[i]), end='')
            number_printed += 1
        except Exception:
            pass
    print('\n', end='')
    return number_printed
