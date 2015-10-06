#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, r):
        self.radius = r
        self.diameter = r * 2
        self.area = math.pi * r * r
