#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle
import pdb

#pdb.set_trace()

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
