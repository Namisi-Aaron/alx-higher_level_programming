#!/usr/bin/python3
"""This module inherits from list"""

class MyList(list):
    """This is a class MyList

    MyList inherits from list
    """
    def print_sorted(self):
        """This method prints a sorted list"""

        print(sorted(self))
