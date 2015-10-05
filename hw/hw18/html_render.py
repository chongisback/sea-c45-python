#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, content=None):
        self.tag = ""
        self.content = []
        if(content is not None):
            self.content.append(content)

    def render(self, f, ind="    ", num=0):
        if(type(self) == Element):
            f.write("\n")
        ind, t_ind = ind * num, ind * (num + 1)
        num += num
        f.write("{ind}<{tag}>\n".format(ind=ind, tag=self.tag))
        print(ind, self.tag)
        for lines in self.content:
            if(type(lines) == Body):
                Body.render(lines, f, num=num)
            elif(type(lines) == P):
                P.render(lines, f, num=num)
            elif(type(lines) == Head):
                Head.render(lines, f, num=num)
            elif(type(lines) == Title):
                Title.render(lines, f, num=num)
            else:
                f.write(t_ind + lines + "\n")
        print(ind, self.tag)
        f.write("{ind}</{tag}>\n".format(ind=ind, tag=self.tag))

    def append(self, text):
        self.content.append(text)


class Html(Element):
    def __init__(self, content=None):
        self.tag = "html"
        self.content = []
        if(content is not None):
            self.content.append(content)

    def render(self, f, ind="    ", num=0):
        ind, t_ind = ind * num, ind * (num + 1)
        num = num + 1
        f.write("<!DOCTYPE html>\n")
        f.write("{ind}<{tag}>\n".format(ind=ind, tag=self.tag))
        print(ind, self.tag)
        for lines in self.content:
            if(type(lines) == Body):
                Body.render(lines, f, num=num)
            elif(type(lines) == P):
                P.render(lines, f, num=num)
            elif(type(lines) == Head):
                Head.render(lines, f, num=num)
            elif(type(lines) == Title):
                Title.render(lines, f, num=num)
            else:
                f.write(t_ind + lines + "\n")
        print(ind, self.tag)
        f.write("{ind}</{tag}>".format(ind=ind, tag=self.tag))


class Body(Element):
    def __init__(self, content=None):
        self.tag = "body"
        self.content = []
        if(content is not None):
            self.content.append(content)


class P(Element):
    def __init__(self, content=None):
        self.tag = "p"
        self.content = []
        if(content is not None):
            self.content.append(content)


class Head(Element):
    def __init__(self, content=None):
        self.tag = "head"
        self.content = []
        if(content is not None):
            self.content.append(content)


class Title(Element):
    def __init__(self, content=None):
        self.tag = "title"
        self.content = []
        if(content is not None):
            self.content.append(content)

    def render(self, f, ind="    ", num=0):
        ind = ind * num
        print(ind, self.tag)
        f.write("{ind}<{tag}>{text}</{tag}>\n\
            ".format(ind=ind, tag=self.tag, text=self.content[0]))
        print(ind, self.tag)
