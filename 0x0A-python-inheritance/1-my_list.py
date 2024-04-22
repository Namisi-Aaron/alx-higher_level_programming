#!/usr/bin/python3
"""Creates a class MyList that inherits from list"""


class MyList(list):
    """defines a class MyList"""

    def print_sorted(self):
        """prints the list in ascending order"""

        print(sorted(self))
