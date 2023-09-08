#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "white")
say_my_name("Bob")
try:
    say_my_name("Bob")
except Exception as e:
    print(e)
