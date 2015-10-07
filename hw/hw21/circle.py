#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, r):
        self._diameter = r * 2
        self.radius = r
        self._area = math.pi * r ** 2

    def __str__(self):
        return 'Circle with radius: {r}'.format(r="%.6f" % self.radius)

    def __repr__(self):
        return 'Circle({r})'.format(r=self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def _getd(self):
        return self._diameter

    def _setd(self, value):
        self._diameter = value
        self.radius = value / 2

    def _deld(self):
        del self._diameter
    diameter = property(_getd, _setd, _deld, doc="docstring")

    def _geta(self):
        return self._area

    area = property(_geta, doc="docstring")
