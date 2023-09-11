#!/usr/bin/python3
"""Module MyList
inherits from list object
"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """prints the list in sorted order"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
