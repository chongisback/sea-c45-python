#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.
class Element(object):

    def __init__(self, name=""):
        self.name = name
        self.children = []
        pass

    def render(self, f):zz
        f.write("<{name}>".format(name=self.name))
        # TODO: Write out the children here
        f.write("</{name}".format(name=self.name))

    def append(self, child):
        self.children.append(child)
    pass
