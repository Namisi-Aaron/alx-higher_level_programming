#!/usr/bin/python3
"""0-safe_print_list
"""

def safe_print_list(my_list=[], x=0):
    """This function prints elements of a list
    and returns the number of elements printed
    """

    number_printed = 0
    for i in range(0, x):
        try:
            print('{}'.format(my_list[i]), end='')
            number_printed += 1
        except Exception:
            pass
    print('\n', end='')
    return number_printed
