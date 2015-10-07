#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math

class Circle(object):
    def __init__(self, r):
        self.radius = r
        self.diameter = r * 2
        self.area = math.pi * r ** 2

    def _get_diameter(self):
        return self._diameter

    def _set_diameter(self, value):
        self._diameter = value
        self._raidus = value / 2

    def _del_diameter(self):
        del self._diameter
    x = property(_get_diameter, _set_diameter, _del_diameter, doc="docstring")
