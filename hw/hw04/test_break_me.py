#!/usr/bin/env python

"""
code that tests the break_me.py functions
"""

# import pytest  # used for the exception testing


import break_me

# bad variable name
def test_name_error():
    try:
        break_me.exhibit_name_error()
        assert(False)
    except NameError:
        assert(True)

# member of variable ex. math.kevin
def test_attribute_error():
    assert('exhibit_attribute_error' in dir(break_me))
    try:
        break_me.exhibit_attribute_error()
        assert(False)
    except AttributeError:
        assert(True)

# type error adding two variable of two types
def test_type_error():
    try:
        break_me.exhibit_type_error()
        assert(False)
    except TypeError:
        assert(True)
