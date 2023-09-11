#!/usr/bin/python3
"""Module 100-my_int
Creates a class that inherits from int
"""


class MyInt(int):
    """Class that inherits from int
    But reverses behaviours of == and !=
    """

    def __eq__(self, other):
        """Equal becomes not equal"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal becomes equal"""

        return super().__eq__(other)
