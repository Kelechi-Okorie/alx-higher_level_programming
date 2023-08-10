#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
mod = number % 10
print(f"Last digit of {number} is {mod}", end="")
if mod > 5:
    print(f" and is greater than 5")
elif mod == 0:
    print(f" and is 0")
elif mod < 6 and mod != 0:
    print(f" and is less than 6 and not 0")
