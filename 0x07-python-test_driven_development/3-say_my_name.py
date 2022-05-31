#!/usr/bin/python3
'''this function allows you to print the
name and surname or only if you add the name
the way of use is as follows
say_my_name("John", "Smith")
My name is John Smith'''


def say_my_name(first_name, last_name=""):
    '''this function evaluates if the
    name and the following name is a
    string otherwise it returns a type error'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
