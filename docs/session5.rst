
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.


***************************************************************************
Session Five: Exceptions, Files, Arguments, Comprehensions
***************************************************************************


Review/Questions
================

.. rst-class:: left
.. container::

    .. rst-class:: build

        * Dictionaries
        * String Formatting
        * Exceptions
        * Files, etc.


Homework Review
---------------

Homework Questions?

Solutions to the dict/set lab, and some others in the class repo in:
``Solutions``

A few tidbits:

.. nextslide:: Sorting Dictionaries:

The ``dict`` isn't sorted, so what if you want to do something in a sorted way?

.. rst-class:: build
.. container::

    The "old" way:

    .. code-block:: python

        keys = d.keys()
        keys.sort()
        for key in keys:
            ...

    .. code-block:: python

        collections.OrderedDict
        sorted()

    (demo)

Exceptions
==========

.. rst-class:: left
.. container::

    Another Branching structure:

    .. code-block:: python

        try:
            do_something()
            f = open('missing.txt')
            process(f)   # never called if file missing
        except IOError:
            print "couldn't open missing.txt"

Exceptions
----------

Never Do this:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except:
        print "couldn't open missing.txt"


Exceptions
----------

Use Exceptions, rather than your own tests:

Don't do this:

.. code-block:: python

    do_something()
    if os.path.exists('missing.txt'):
        f = open('missing.txt')
        process(f)   # never called if file missing

It will almost always work -- but the almost will drive you crazy

.. nextslide::

Example from homework

.. code-block:: python

    if num_in.isdigit():
        num_in = int(num_in)

but -- ``int(num_in)`` will only work if the string can be converted to an integer.

So you can do

.. code-block:: python

    try:
        num_in = int(num_in)
    except ValueError:
        print(u"Input must be an integer, try again.")

Or let the Exception be raised....


.. nextslide:: EAFP

::

    "it's Easier to Ask Forgiveness than Permission"

    -- Grace Hopper

http://www.youtube.com/watch?v=AZDWveIdqjY

(Pycon talk by Alex Martelli)

.. nextslide:: Do you catch all Exceptions?

For simple scripts, let exceptions happen.

Only handle the exception if the code can and will do something about it.

(much better debugging info when an error does occur)


Exceptions -- finally
---------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print(u"couldn't open missing.txt")
    finally:
        do_some_clean-up

The ``finally:``  clause will always run


Exceptions -- else
-------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError:
        print(u"couldn't open missing.txt")
    else:
        process(f) # only called if there was no exception

Advantage:
  you know where the Exception came from

Exceptions -- using them
------------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError as the_error:
        print the_error
        the_error.extra_info = "some more information"
        raise

.. rst-class:: build
.. container::

    Particularly useful if you catch more than one exception:

    .. code-block:: python

        except (IOError, BufferError, OSError) as the_error:
            do_something_with (the_error)


Raising Exceptions
------------------

.. code-block:: python

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("b can not be zero")
        else:
            return a / b

.. rst-class:: build
.. container::

    when you call it:

    .. code-block:: ipython

        In [515]: divide (12,0)
        ZeroDivisionError: b can not be zero


Built in Exceptions
-------------------

You can create your own custom exceptions, but...

.. rst-class:: build
.. container::

    .. code-block:: python

        exp = [name for name in dir(__builtin__) if "Error" in name]
        len(exp)
        32

    For the most part, you can/should use a built in one

.. nextslide::

Choose the best match you can for the built in Exception you raise.

.. rst-class:: build
.. container::

    Example (for last week's ackerman homework)::

        if (not isinstance(m, int)) or (not isinstance(n, int)):
            raise ValueError

    Is the *value* of the input the problem here?

    Nope: the *type* is the problem::

        if (not isinstance(m, int)) or (not isinstance(n, int)):
            raise TypeError

    but should you be checking type anyway? (EAFP)


File Reading and Writing
========================

Files
-----

Text Files

.. code-block:: python

    import io
    f = io.open('secrets.txt', encoding='utf-8')
    secret_data = f.read()
    f.close()

``secret_data`` is a (unicode) string

``encoding`` defaults to ``sys.getdefaultencoding()`` -- often NOT what you
want.

(There is also the regular ``open()`` built in, but it won't handle Unicode for
you...)

.. nextslide::

Binary Files

.. code-block:: python

    f = io.open('secrets.bin', 'rb')
    secret_data = f.read()
    f.close()

``secret_data``  is a byte string

(with arbitrary bytes in it -- well, not arbitrary -- whatever is in the file.)

(See the ``struct``  module to unpack formatted binary data)


.. nextslide::

File Opening Modes

.. code-block:: python

    f = io.open('secrets.txt', [mode])
    'r', 'w', 'a'
    'rb', 'wb', 'ab'
    r+, w+, a+
    r+b, w+b, a+b
    U
    U+

These follow the Unix conventions, and aren't all that well documented on the
Python docs. But these BSD docs make it pretty clear:

http://www.manpagez.com/man/3/fopen/

**Gotcha** -- 'w' modes always clear the file

.. nextslide:: Text File Notes

Text is default

* Newlines are translated: ``\r\n -> \n``
*   -- reading and writing!
* Use \*nix-style in your code: ``\n``
* ``io.open()`` returns various "stream" objects -- but they act like file
  objects.
* In text mode, io.open() defaults to "Universal" newline mode.


Gotcha:

* no difference between text and binary on \*nix
* breaks on Windows


.. nextslide:: Other parameters to ``io.open()``:

``io.open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)``

* ``file`` is generally a file name or full path

* ``mode`` is the mode for opening: 'r', 'w', etc.

* ``buffering`` controls the buffering mode (0 for no buffering)

* ``encoding`` sets the unicode encoding -- only for text files -- when set,
  you can ONLY write unicode object to the file.

* ``errors`` sets the encoding error mode: 'strict', 'ignore', 'replace',...

* ``newline`` controls Universal Newline mode: lets you write DOS-type files on
  \*nix, for instance (text mode only).

* ``closedfd`` controls close()  behavior if a file descriptor, rather than a
  name is passed in (advanced usage!)

(https://docs.python.org/2/library/io.html?highlight=io.open#io.open)


File Reading
------------

Reading part of a file

.. code-block:: python

    header_size = 4096
    f = open('secrets.txt')
    secret_header = f.read(header_size)
    secret_rest = f.read()
    f.close()

.. nextslide::


Common Idioms

.. code-block:: python

    for line in io.open('secrets.txt'):
        print line

.. rst-class:: build
.. container::

    (the file object is an iterator!)

    .. code-block:: python

        f = io.open('secrets.txt')
        while True:
            line = f.readline()
            if not line:
                break
            do_something_with_line()


File Writing
------------

.. code-block:: python

    outfile = io.open('output.txt', 'w')
    for i in range(10):
        outfile.write("this is line: %i\n"%i)


File Methods
------------

Commonly Used Methods

.. code-block:: python

    f.read() f.readline() f.readlines()

    f.write(str) f.writelines(seq)

    f.seek(offset) f.tell()

    f.flush()

    f.close()


File Like Objects
-----------------


Many classes implement the file interface:

.. rst-class:: build

* loggers
* ``sys.stdout``
* ``urllib.open()``
* pipes, subprocesses
* StringIO

https://docs.python.org/2/library/stdtypes.html#file-objects

StringIO
--------

.. code-block:: python

    In [417]: import StringIO
    In [420]: f = StringIO.StringIO()
    In [421]: f.write(u"somestuff")
    In [422]: f.seek(0)
    In [423]: f.read()
    Out[423]: 'somestuff'

(handy for testing file handling code...)


Paths and Directories
=====================

Paths
-----

Paths are generally handled with simple strings (or Unicode strings)

Relative paths:

.. code-block:: python

    u'secret.txt'
    u'./secret.txt'

Absolute paths:

.. code-block:: python

    u'/home/chris/secret.txt'


Either work with ``open()`` , etc.

(working directory only makes sense with command-line programs...)

os module
----------

.. code-block:: python

    os.getcwd() -- os.getcwdu() (u for Unicode)
    chdir(path)
    os.path.abspath()
    os.path.relpath()￼


.. nextslide:: os.path module

.. code-block:: python

    os.path.split()
    os.path.splitext()
    os.path.basename()
    os.path.dirname()
    os.path.join()


(all platform independent)

.. nextslide:: directories

.. code-block:: python

    os.listdir()
    os.mkdir()
    os.walk()

(higher level stuff in ``shutil``  module)

pathlib
-------

``pathlib`` is a new package for handling paths in an OO way:

http://pathlib.readthedocs.org/en/pep428/

It is now part of the Python3 standard library, and has been back-ported for use with Python2:

.. code-block:: bash

    $ pip install pathlib

.. nextslide::

All the stuff in os.path and more:

.. code-block:: ipython

    In [64]: import pathlib
    In [65]: pth = pathlib.Path('./')
    In [66]: pth.is_dir()
    Out[66]: True
    In [67]: pth.absolute()
    Out[67]: PosixPath('/Users/Chris/PythonStuff/CodeFellowsClass/sea-f2-python-sept14/Examples/Session04')
    In [68]: for f in pth.iterdir():
                 print f
    junk2.txt
    junkfile.txt
    ...

Puzzle and Mid-point Activities
===============================

* Check in attendance.
* Copy and paste your HW 12 (Dictionary and Files) homework code from
Interactive Python textbook into Canvas.
* Puzzle: Fizzbuzz

* Look up the ``%``  operator. What is the value of the following?

  * ``10 % 7 == 3``
  * ``14 % 7 == 0``

* Write a program that prints the numbers from 1 to 100 inclusive. But for
  multiples of three print "Fizz" instead of the number and for the multiples
  of five print "Buzz". For numbers which are multiples of both three and five
  print "FizzBuzz" instead.


Advanced Argument Passing
=========================

Keyword arguments
-----------------

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [150]: from __future__ import print_function
    In [151]: def fun(x, y=0, z=0):
       .....:     print(x, y, z, end=" ")
       .....:
    In [152]: fun(1, 2, 3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(1, z=3, y=2)
    1 2 3

.. nextslide::

A Common Idiom:

.. code-block:: python

    def fun(x, y=None):
        if y is None:
            do_something_different
        go_on_here

.. nextslide::

Can set defaults to variables

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print(u"x is: %s" % x)
       .....:
    In [158]: fun()
    x is: 4

.. nextslide:: But Remember

Defaults are evaluated when the function is defined

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print(u"x is: %s" % x)
       .....:
    In [158]: fun()
    x is: 4
    In [159]: y = 6
    In [160]: fun()
    x is: 4

Function arguments in variables
-------------------------------

function arguments are really just:

.. rst-class:: build
.. container::

    * a tuple (positional arguments)
    * a dict (keyword arguments)

    .. code-block:: python

        In [1]: def f(x, y, w=0, h=0):
           ...:     msg = u"position: %s, %s -- shape: %s, %s"
           ...:     print(msg % (x, y, w, h))
           ...:
        In [2]: position = (3, 4)
        In [3]: size = {'h': 10, 'w': 20}
        In [4]: f(*position, **size)
        position: 3, 4 -- shape: 20, 10

Function parameters in variables
--------------------------------

You can also pull the parameters out in the function as a tuple and a dict:

.. code-block:: ipython

    In [10]: def f(*args, **kwargs):
       ....:     print(u"the positional arguments are: %s" % unicode(args))
       ....:     print(u"the optional arguments are: %s" % unicode(kwargs))
       ....:
    In [11]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the optional arguments are: {'this': 5, 'that': 7}

Passing a dict to the ``string.format()`` method
------------------------------------------------

Now that you know that keyword args are really a dict, you can do this nifty
trick:

.. rst-class:: build
.. container::

    .. container::

        The ``format`` method takes keyword arguments:

        .. code-block:: ipython

            In [24]: u"My name is {first} {last}".format(last=u"Ewing", first=u"Cris")
            Out[24]: u'My name is Cris Ewing'

    .. container::

        Build a dict of the keys and values:

        .. code-block:: ipython

            In [25]: d = {u"last": u"Ewing", u"first": u"Cris"}

    .. container::

        And pass to ``format()``with ``**``

        .. code-block:: ipython

            In [26]: u"My name is {first} {last}".format(**d)
            Out[26]: u'My name is Cris Ewing'

LAB
---

Let's do this right now:

.. rst-class:: build
.. container::

    keyword arguments

    .. rst-class:: build

        * Write a function that has four optional parameters (with defaults):

          - foreground_color
          - background_color
          - link_color
          - visited_link_color

        * Have it print the colors (use strings for the colors)
        * Call it with a couple different parameters set
        * Have it pull the parameters out with ``*args, **kwargs``


A bit more on mutability (and copies)
=====================================

.. rst-class:: left

We've talked about this: mutable objects can have their contents changed in
place.

.. rst-class:: left build
.. container::

    Immutable objects can not.

    This has implications when you have a container with mutable objects in it:

    .. code-block:: ipython

        In [28]: list1 = [ [1,2,3], ['a','b'] ]

    one way to make a copy of a list:

    .. code-block:: ipython

        In [29]: list2 = list1[:]
        In [30]: list2 is list1
        Out[30]: False

    they are different lists.

mutable objects
---------------

What if we set an element to a new value?

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [31]: list1[0] = [5,6,7]

        In [32]: list1
        Out[32]: [[5, 6, 7], ['a', 'b']]

        In [33]: list2
        Out[33]: [[1, 2, 3], ['a', 'b']]

    So they are independent.

.. nextslide::

But what if we mutate an element?

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [34]: list1[1].append('c')

        In [35]: list1
        Out[35]: [[5, 6, 7], ['a', 'b', 'c']]

        In [36]: list2
        Out[36]: [[1, 2, 3], ['a', 'b', 'c']]

    uh oh! mutating an element in one list mutated the one in the other list.

.. nextslide::

Why is that?

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [38]: list1[1] is list2[1]
        Out[38]: True

    The elements are the same object!

    This is known as a "shallow" copy -- Python doesn't want to copy more than
    it needs to, so in this case, it makes a new list, but does not make copies
    of the contents.

    Same for dicts (and any container type)

    If the elements are immutable, it doesn't really make a differnce -- but be
    very careful with mutable elements.


The copy module
--------------------

most objects have a way to make copies (``dict.copy()`` for instance).

.. rst-class:: build
.. container::

    but if not, you can use the ``copy`` module to make a copy:

    .. code-block:: ipython

        In [39]: import copy

        In [40]: list3 = copy.copy(list2)

        In [41]: list3
        Out[41]: [[1, 2, 3], ['a', 'b', 'c']]

    This is *also* a shallow copy.

.. nextslide::

But there is another option:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [3]: list1
        Out[3]: [[1, 2, 3], ['a', 'b', 'c']]

        In [4]: list2 = copy.deepcopy(list1)

        In [5]: list1[0].append(4)

        In [6]: list1
        Out[6]: [[1, 2, 3, 4], ['a', 'b', 'c']]

        In [7]: list2
        Out[7]: [[1, 2, 3], ['a', 'b', 'c']]

    ``deepcopy`` recurses through the object, making copies of everything as it goes.

.. nextslide::

I happened on this thread on stack overflow:

http://stackoverflow.com/questions/3975376/understanding-dict-copy-shallow-or-deep

.. rst-class:: build
.. container::

    The OP is pretty confused -- can you sort it out?

    Make sure you understand the difference between a reference, a shallow
    copy, and a deep copy.

Mutables as default arguments:
------------------------------

Another "gotcha" is using mutables as default arguments:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [11]: def fun(x, a=[]):
           ....:     a.append(x)
           ....:     print(a)
           ....:

    This makes sense: maybe you'd pass in a list, but the default is an empty list.

    .. container::

        But:

        .. code-block:: ipython

            In [12]: fun(3)
            [3]

            In [13]: fun(4)
            [3, 4]

    Huh?!

.. nextslide::

Remember:

.. rst-class:: build

* the default argument is defined when the function is created
* there will be *only one list*
* every time the function is called, the *same one list* is used.

.. rst-class:: build
.. container::

    The standard practice for such a mutable default argument:

    .. code-block:: ipython

        In [15]: def fun(x, a=None):
           ....:     if a is None:
           ....:         a = []
           ....:     a.append(x)
           ....:     print(a)
        In [16]: fun(3)
        [3]
        In [17]: fun(4)
        [4]

    You get a new list every time the function is called


List and Dict Comprehensions
============================

.. rst-class:: left
.. container::

    A bit of functional programming

    .. rst-class:: build
    .. container::

        consider this common ``for`` loop structure:

        .. code-block:: python

            new_list = []
            for variable in a_list:
                new_list.append(expression)

        This can be expressed with a single line using a "list comprehension"

        .. code-block:: python

            new_list = [expression for variable in a_list]

List Comprehensions
-------------------

What about nested for loops?

.. rst-class:: build
.. container::

    .. code-block:: python

        new_list = []
        for var in a_list:
            for var2 in a_list2:
                new_list.append(expression)

    Can also be expressed in one line:

    .. code-block:: python

        new_list =  [exp for var in a_list for var2 in a_list2]

    You get the "outer product", i.e. all combinations.

    (demo)

.. nextslide::

But usually you at least have a conditional in the loop:

.. rst-class:: build
.. container::

    .. code-block:: python

        new_list = []
        for variable in a_list:
            if something_is_true:
                new_list.append(expression)

    You can add a conditional to the comprehension:

    .. code-block:: python

        new_list = [expr for var in a_list if something_is_true]

    (demo)

.. nextslide::

Examples:

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [341]: [x ** 2 for x in range(3)]
        Out[341]: [0, 1, 4]

        In [342]: [x + y for x in range(3) for y in range(5, 7)]
        Out[342]: [5, 6, 6, 7, 7, 8]

        In [343]: [x * 2 for x in range(6) if not x % 2]
        Out[343]: [0, 4, 8]

    Remember this from last week?

    .. code-block:: python

        [name for name in dir(__builtin__) if "Error" in name]
        ['ArithmeticError',
         'AssertionError',
         'AttributeError',
         ....


Set Comprehensions
------------------

You can do it with sets, too:

.. rst-class:: build
.. container::

    .. code-block:: python

        new_set = {value for value in a_sequence}


    the same as this ``for`` loop:

    .. code-block:: python

        new_set = set()
        for value in a_sequence:
            new_set.add(value)

.. nextslide::

Example: finding all the vowels in a string...

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [19]: s = "a not very long string"

        In [20]: vowels = set('aeiou')

        In [21]: { let for let in s if let in vowels }
        Out[21]: {'a', 'e', 'i', 'o'}

    Side note: why did I do ``set('aeiou')`` rather than just `aeiou`\ ?


Dict Comprehensions
-------------------

Also with dictionaries

.. rst-class:: build
.. container::

    .. code-block:: python

        new_dict = { key:value for key, value in a_sequence}


    the same as this ``for`` loop:

    .. code-block:: python

        new_dict = {}
        for key, value in a_sequence:
            new_dict[key] = value

.. nextslide::

Example

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [22]: {i: "this_%i" % i for i in range(5)}
        Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
                  3: 'this_3', 4: 'this_4'}

    Can you do the same thing with the ``dict()`` constructor?


Anonymous functions
===================

.. rst-class:: center large

λ

lambda
------

.. code-block:: ipython

    In [171]: f = lambda x, y: x+y
    In [172]: f(2,3)
    Out[172]: 5

.. rst-class:: build
.. container::

    Content can only be an expression -- not a statement

    Anyone remember what the difference is?

    Called "Anonymous": it doesn't need a name.

.. nextslide::

It's a python object, it can be stored in a list or other container

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [6]: l = [lambda x, y: x + y]

        In [7]: l
        Out[7]: [<function __main__.<lambda>>]

        In [8]: type(l[0])
        Out[8]: function


    And you can call it:

    .. code-block:: ipython

        In [9]: l[0](3,4)
        Out[9]: 7


Functions as first class objects
---------------------------------

You can do that with "regular" functions too:

.. code-block:: ipython

    In [12]: def fun(x,y):
       ....:     return x + y
       ....:
    In [13]: l = [fun]
    In [14]: type(l[0])
    Out[14]: function
    In [15]: l[0](3, 4)
    Out[15]: 7


Functional Programming
======================

map
---

``map``: "maps" a function onto a sequence of objects -- It applies the
function to each item in the list, returning another list

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [23]: l = [2, 5, 7, 12, 6, 4]
        In [24]: def fun(x):
                     return x * 2 + 10
        In [25]: map(fun, l)
        Out[25]: [14, 20, 24, 34, 22, 18]


    But if it's a small function, and you only need it once:

    .. code-block:: ipython

        In [26]: map(lambda x: x * 2 + 10, l)
        Out[26]: [14, 20, 24, 34, 22, 18]


filter
------

``filter``: "filters" a sequence of objects with a boolean function -- It keeps
only those for which the function is True

.. rst-class:: build
.. container::

    To get only the even numbers:

    .. code-block:: ipython

        In [27]: l = [2, 5, 7, 12, 6, 4]
        In [28]: filter(lambda x: not x % 2, l)
        Out[28]: [2, 12, 6, 4]

reduce
------

``reduce``: "reduces" a sequence of objects to a single object with a function
that combines two arguments

.. rst-class:: build
.. container::

    To get the sum:

    .. code-block:: ipython

        In [30]: l = [2, 5, 7, 12, 6, 4]
        In [31]: reduce(lambda x, y: x + y, l)
        Out[31]: 36

    To get the product:

    .. code-block:: ipython

        In [32]: reduce(lambda x,y: x*y, l)
        Out[32]: 20160

Comprehensions
--------------

Couldn't you do all this with comprehensions?

.. rst-class:: build
.. container::

    Yes:

    .. code-block:: ipython

        In [33]: [x + 2 + 10 for x in l]
        Out[33]: [14, 17, 19, 24, 18, 16]
        In [34]: [x for x in l if not x % 2]
        Out[34]: [2, 12, 6, 4]

    (Except Reduce)

    But Guido thinks almost all uses of reduce are really ``sum()``

Functional Programming
----------------------

Comprehensions and map, filter, reduce are all "functional programming"
approaches}

.. rst-class:: build
.. container::

    ``map, filter``  and ``reduce``  pre-date comprehensions in Python's history

    Some people like that syntax better

    And "map-reduce" is a big concept these days for parallel processing of "Big
    Data" in NoSQL databases.

    (Hadoop, EMR, MongoDB, etc.)

More About Lambda
-----------------

Can also use keyword arguments

.. rst-class:: build
.. container::

    .. code-block:: ipython

        In [186]: l = []
        In [187]: for i in range(3):
           .....:     l.append(lambda x, e=i: x**e)
           .....:
        In [189]: for f in l:
           .....:     print(f(3))
        1
        3
        9

    Note when the keyword argument is evaluated

    This turns out to be very handy!


Recommended Reading
---------------------

* LPTHW: Ex 40 - 45

http://learnpythonthehardway.org/book/

* Dive Into Python: chapter 4, 5

http://www.diveintopython.net/toc/index.html

