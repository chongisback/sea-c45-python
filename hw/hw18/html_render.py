#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, tag="", content=None, id="", style=""):
        self.tag = tag
        self.content = []
        self.id = id
        self.style = style
        if(content is not None):
            self.content.append(content)

    def render(self, f, ind="    ", num=0):
        """
        Renders html tags and content to a page
        """
        # Step 2 and 3 have <!DOCTYPE html> for html page
        if(type(self) == Html):
            f.write("<!DOCTYPE html>")
        # Algorithm for indentation. Indentation is 4 spaces
        # and is multiplied by 1 higher number when nested to the next tag
        # t_ind is for the line that has content such as <p>
        ind, t_ind = ind * num, ind * (num + 1)
        num += 1
        if(self.style != ""):
            f.write('\n{ind}<{tag} style="{style}">'.format(ind=ind,
                                                            tag=self.tag,
                                                            style=self.style))
        else:
            f.write("\n{ind}<{tag}>".format(ind=ind, tag=self.tag))

        for lines in self.content:
            # If type of the line is not a string, it will render
            # with the class of object it is. It will also pass number of tabs
            if(type(lines) != str):
                type(lines).render(lines, f, num=num)
            # If it is a string, it will write out a content with
            # a new line, and +1 indentation and string
            else:
                f.write("\n{ind}{text}".format(ind=t_ind, text=lines))
        # Writes closing tag
        f.write("\n{ind}</{tag}>".format(ind=ind, tag=self.tag))

    def append(self, text):
        self.content.append(text)


class Html(Element):
    def __init__(self):
        super(Html, self).__init__(tag="html")


class Body(Element):
    def __init__(self):
        super(Body, self).__init__(tag="body")


class P(Element):
    def __init__(self, content=None, style=""):
        super(P, self).__init__(tag="p", content=content, style=style)


class Head(Element):
    def __init__(self):
        super(Head, self).__init__(tag="head")


class Title(Element):
    def __init__(self, content=None):
        super(Title, self).__init__(tag="title", content=content)

    def render(self, f, ind="    ", num=0):
        ind = ind * num
        f.write("\n{ind}<{tag}>{text}</{tag}>".format(ind=ind,
                                                      tag=self.tag,
                                                      text=self.content[0]))


class SelfClosingTag(Element):
    def __init__(self, tag=""):
        self.tag = tag
        super(SelfClosingTag, self).__init__(tag=tag)

    def render(self, f, ind="    ", num=0):
        ind = ind * num
        f.write("\n{ind}<{tag} />".format(ind=ind, tag=self.tag))


class Hr(SelfClosingTag):
    def __init__(self):
        super(Hr, self).__init__(tag="hr")


class Br(SelfClosingTag):
    def __init__(self):
        super(Br, self).__init__(tag="br")


class A(Element):
    def __init__(self, l, c):
        self.l = l
        super(A, self).__init__(tag="a", content=c)

    def render(self, f, ind="    ", num=0):
        ind = ind * num
        f.write('\n{i}<{t} href="{l}">{c}</{t}>'.format(i=ind,
                                                        t=self.tag,
                                                        l=self.l,
                                                        c=self.content[0]))
