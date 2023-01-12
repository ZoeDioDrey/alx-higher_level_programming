#!/usr/bin/python3
"""Define a class that checks for the same object"""

def is_same_class(obj, a_class):
    """function to check if obj is the same class
    Arguments:
        param1: obj
        param2: a_class that matches the obj
    Return:
    True for isinstance of obj or False if not
    """

    if type(obj) == a_class:
        return True
    else:
        return False
