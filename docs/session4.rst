.. Foundations 2: Python slides file, created by
   Chris Barker: May 12, 2014.

*******************************************************
Session Four: More Iteration, Strings, Dictionaries
*******************************************************

Feedback Surveys
================

What's Going Well
-----------------
* Office hours before each class
* Lab sessions with TA's
* Practicing git by submitting homework
* Working with classmates

.. nextslide::

What's Challenging
-----------------
* HW 05 (setting up shell customizations) is hard
* HW 07 (recursion) more preparation needed
* Difficulties with paths on Windows machines
* A lot of background assumed for Unix & Git
* Material is going by really quick
* Easier intro class? (Yes, F1 or 201)
* Need links to slides at home.

Link to Course Notes
-----------------

These are the same as the slides!
http://codefellows.github.io/sea-c45-python

Review/Questions
================

Review and Extension of Previous Class
--------------------------

.. rst-class:: build

* Sequences

  - Slicing
  - Lists
  - Tuples
  - tuple vs lists - which to use?

* interating

  - for
  - while

    - break and continue

  - else with loops

.. container::

    Any questions?

.. nextslide::

.. nextslide:: No Namespace

Be alert that a loop does not create a local namespace:

.. code-block:: ipython

    In [172]: x = 10
    In [173]: for x in range(3):
       .....:     pass
       .....:
    In [174]: x
    Out[174]: 2


.. nextslide:: Loop Control

Sometimes you want to interrupt or alter the flow of control through a loop.

Loops can be controlled in two ways, with ``break`` and ``continue``


.. nextslide:: Break

The ``break`` keyword will cause a loop to immediately terminate:

.. code-block:: ipython

    In [141]: for i in range(101):
       .....:     print(i)
       .....:     if i > 50:
       .....:         break
       .....:
    0 1 2 3 4 5... 46 47 48 49 50 51

.. nextslide:: Continue

The ``continue`` keyword will skip later statements in the loop block, but
allow iteration to continue:

.. code-block:: ipython

    In [143]: for in in range(101):
       .....:     if i > 50:
       .....:         break
       .....:     if i < 25:
       .....:         continue
       .....:     print(i),
       .....:
       25 26 27 28 29 ... 41 42 43 44 45 46 47 48 49 50

.. nextslide:: Else

For loops can also take an optional ``else`` block.

Executed only when the loop exits normally (not via break):

.. code-block:: ipython

    In [147]: for x in range(10):
       .....:     if x == 11:
       .....:         break
       .....: else:
       .....:     print(u'finished')
    finished
    In [148]: for x in range(10):
       .....:     if x == 5:
       .....:         print(x)
       .....:         break
       .....: else:
       .....:     print(u'finished')
    5

This is a really nice unique Python feature!

While Loops
-----------

The ``while`` keyword is for when you don't know how many loops you need.

It continues to execute the body until condition is not ``True``::

    while a_condition:
       some_code
       in_the_body

.. nextslide:: ``while`` vs. ``for``

``while``  is more general than ``for``

-- you can always express ``for`` as ``while``,

but not always vice-versa.

``while``  is more error-prone -- requires some care to terminate

loop body must make progress, so condition can become ``False``

potential error -- infinite loops:

.. code-block:: python

    i = 0;
    while i < 5:
        print(i)


.. nextslide:: Terminating a while Loop

Use ``break``:

.. code-block:: ipython

    In [150]: while True:
       .....:     i += 1
       .....:     if i > 10:
       .....:         break
       .....:     print(i, end=' ')
       .....:
    1 2 3 4 5 6 7 8 9 10

.. nextslide:: Terminating a while Loop

Set a flag:

.. code-block:: ipython

    In [156]: import random
    In [157]: keep_going = True
    In [158]: while keep_going:
       .....:     num = random.choice(range(5))
       .....:     print(num)
       .....:     if num == 3:
       .....:         keep_going = False
       .....:
    3

.. nextslide:: Terminating a While Loop

Use a condition:

.. code-block:: ipython

    In [161]: while i < 10:
       .....:     i += random.choice(range(4))
       .....:     print(i)
       .....:
    0 0 2 3 4 6 8 8 8 9 12


Similarities
------------

Both ``for`` and ``while`` loops can use ``break`` and ``continue`` for
internal flow control.

Both ``for`` and ``while`` loops can have an optional ``else`` block

In both loops, the statements in the ``else`` block are only executed if the
loop terminates normally (no ``break``)


User Input
==============

.. rst-class:: left

For some of your homework, you'll need to interact with a user at the
command line.

.. rst-class:: left

There's a nice builtin function to do this - ``input``:

.. rst-class:: left

.. code-block:: python

    In [196]: fred = raw_input(u'type something-->')
    type something-->;alksdjf
    In [197]: fred
    Out[197]: ';alksdjf'

.. rst-class:: left

This will display a prompt to the user, allowing them to input text and
allowing you to bind that input to a symbol.

Pair Programming
================

With a partner, write a guessing game that repeatedly asks the user
to guess a number from 1 to 100 until they get the number correct.
If the guess is too high, print "Too high!".
If the guess is too low, print "Too low!".
Otherwise, print "Congrats! You're a winner."


String Features
=================

.. rst-class:: center large

  Fun with Strings


Manipulations
-------------

``split`` and ``join``:

.. code-block:: ipython

    In [167]: csv = "comma, separated, values"
    In [168]: csv.split(', ')
    Out[168]: ['comma', 'separated', 'values']
    In [169]: psv = '|'.join(csv.split(', '))
    In [170]: psv
    Out[170]: 'comma|separated|values'


.. nextslide:: Case Switching

.. code-block:: ipython

    In [171]: sample = u'A long string of words'
    In [172]: sample.upper()
    Out[172]: u'A LONG STRING OF WORDS'
    In [173]: sample.lower()
    Out[173]: u'a long string of words'
    In [174]: sample.swapcase()
    Out[174]: u'a LONG STRING OF WORDS'
    In [175]: sample.title()
    Out[175]: u'A Long String Of Words'


.. nextslide:: Testing

.. code-block:: ipython

    In [181]: number = u"12345"
    In [182]: number.isnumeric()
    Out[182]: True
    In [183]: number.isalnum()
    Out[183]: True
    In [184]: number.isalpha()
    Out[184]: False
    In [185]: fancy = u"Th!$ $tr!ng h@$ $ymb0l$"
    In [186]: fancy.isalnum()
    Out[186]: False


Ordinal values
--------------

"ASCII" values: 1-127

"ANSI" values: 1-255

To get the value:

.. code-block:: ipython

    In [109]: for i in 'Chris':
       .....:     print(ord(i), end=' ')
    67 104 114 105 115
    In [110]: for i in (67,104,114,105,115):
       .....:     print(chr(i), end=' ')
    C h r i s


Building Strings
----------------

You can, but please don't do this:

.. code-block:: python

    'Hello ' + name + '!'

Do this instead:

.. code-block:: python

    'Hello %s!' % name

It's much faster and safer, and easier to modify as code gets complicated.

http://docs.python.org/library/stdtypes.html#string-formatting-operations


.. nextslide:: String Formatting

The string format operator: ``%``

.. code-block:: ipython

    In [261]: u"an integer is: %i" % 34
    Out[261]: u'an integer is: 34'
    In [262]: u"a floating point is: %f" % 34.5
    Out[262]: u'a floating point is: 34.500000'
    In [263]: u"a string is: %s" % u"anything"
    Out[263]: u'a string is: anything'

.. nextslide:: More Placeholders

Multiple placeholders:

.. code-block:: ipython

    In [264]: u"the number %s is %i" % (u'five', 5)
    Out[264]: u'the number five is 5'
    In [266]: u"the first 3 numbers are: %i, %i, %i" % (1,2,3)
    Out[266]: u'the first 3 numbers are: 1, 2, 3'

The counts must agree:

.. code-block:: ipython

    In [187]: u"string with %i formatting %s" % (1, )
    ---------------------------------------------------------------------------
    ...
    TypeError: not enough arguments for format string


.. nextslide::

Named placeholders:

.. code-block:: ipython

    In [191]: u"Hello, %(name)s, whaddaya know?" % {u'name': "Joe"}
    Out[191]: u'Hello, Joe, whaddaya know?'

You can use values more than once, and skip values:

.. code-block:: ipython

    In [193]: u"Hi, %(name)s. Howzit, %(name)s?" % {u'name': u"Bob", u'age': 27}
    Out[193]: u'Hi, Bob. Howzit, Bob?'


.. nextslide:: New Formatting

In more recent versions of Python (2.6+) this is `being phased out`_ in favor of the ``.format()`` method on strings.

.. code-block:: ipython

    In [194]: u"Hello, {}, how's your {}".format(u"Bob", u"wife")
    Out[194]: u"Hello, Bob, how's your wife"
    In [195]: u"Hi, {name}. How's your {relation}?".format(name=u'Bob', relation=u'wife')
    Out[195]: u"Hi, Bob. How's your wife?"


.. nextslide:: Complex Formatting

For both of these forms of string formatting, there is a complete syntax for
specifying all sorts of options.

It's well worth your while to spend some time getting to know this
`formatting language`_. You can accomplish a great deal just with this.

.. _formatting language: https://docs.python.org/2/library/string.html#format-specification-mini-language

.. _being phased out: https://docs.python.org/2/library/stdtypes.html#str.format


A couple other nifty utilties with for loops:

**tuple unpacking:**

remember this?

.. code-block:: python

    x, y = 3, 4

You can do that in a for loop, also:

.. code-block:: ipython

    In [3]: from __future__ import print_function
    In [4]: l = [(1, 2), (3, 4), (5, 6)]
    In [5]: for i, j in l:
                print("i:%i, j:%i" % (i, j))

    i:1, j:2
    i:3, j:4
    i:5, j:6

Looping through two loops at once:
----------------------------------

**zip:**

.. code-block:: ipython

    In [10]: l1 = [1, 2, 3]
    In [11]: l2 = [3, 4, 5]
    In [12]: for i, j in zip(l1, l2):
       ....:     print("i:%i, j:%i" % (i, j))
       ....:
    i:1, j:3
    i:2, j:4
    i:3, j:5



Homework comments
-----------------

Building up a long string.

The obvious thing to do is something like::

    msg = u""
    for piece in list_of_stuff:
        msg += piece

But: strings are immutable -- python needs to create a new string each time you
add a piece -- not efficient::

    msg = []
    for piece in list_of_stuff:
        msg.append(piece)
    u" ".join(msg)

appending to lists is efficient -- and so is the join() method of strings.

.. nextslide::

What is ``assert`` for?

Testing -- NOT for issues expected to happen operationally::

    assert m >= 0

in operational code should be::

    if m < 0:
        raise ValueError

I'll cover Exceptions later this class...

(Asserts get ignored if optimization is turned on!)


A little warm up
=================

Fun with strings
------------------

* Rewrite: ``the first 3 numbers are: %i, %i, %i"%(1,2,3)``

  - for an arbitrary number of numbers...

* Write a format string that will take:

  - ``( 2, 123.4567, 10000)``

  - and produce:

  - `` "file_002 :   123.46, 1e+04" ``

Homework Review
======================

Someone volunteer to have their HW 8 debugged in class.

Design critique in class.


Today's Puzzle: Trigrams
========================

N-grams are a way to study word associations

https://books.google.com/ngrams

.. nextslide::

* Coding Kata 14 - Dave Thomas

  http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

  and in this doc:

  http://codefellows.github.io/sea-c45-python/supplements/kata_fourteen.html

* Use "The Travels of Marco Polo the Venetian" as input:

  http://codefellows.github.io/sea-c34-python/_downloads/marco-polo.txt

.. nextslide::

* Our task today: read in the words from a large text file,
  create a dictionary of trigrams.

* Write pseudo code and create a design.

* Use dictionaries, exceptions, file reading/writing.



Dictionaries and Sets
=====================

Dictionary
----------

Python calls it a ``dict``

Other languages call it:

* dictionary
* associative array
* map
* hash table
* hash
* key-value pair


Dictionary Constructors
-----------------------

.. code-block:: python

    >>> {'key1': 3, 'key2': 5}
    {'key1': 3, 'key2': 5}
    >>> dict([('key1', 3),('key2', 5)])
    {'key1': 3, 'key2': 5}
    >>> dict(key1=3, key2=5)
    {'key1': 3, 'key2': 5}
    >>> d = {}
    >>> d['key1'] = 3
    >>> d['key2'] = 5
    >>> d
    {'key1': 3, 'key2': 5}

Dictionary Indexing
-------------------

.. code-block:: python

    >>> d = {'name': 'Brian', 'score': 42}
    >>> d['score']
    42
    >>> d = {1: 'one', 0: 'zero'}
    >>> d[0]
    'zero'
    >>> d['non-existing key']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'non-existing key'


.. nextslide::

Keys can be any **immutable** object:

* number
* string
* tuple

.. code-block:: ipython

    In [325]: d[3] = 'string'
    In [326]: d[3.14] = 'pi'
    In [327]: d['pi'] = 3.14
    In [328]: d[ (1,2,3) ] = 'a tuple key'
    In [329]: d[ [1,2,3] ] = 'a list key'
       TypeError: unhashable type: 'list'


Actually -- any "hashable" type.


.. nextslide:: Hashing

Hash functions convert arbitrarily large data to a small proxy (usually int)

.. rst-class:: build
.. container::

    Always return the same proxy for the same input

    MD5, SHA, etc

    Dictionaries hash the key to an integer proxy and use it to find the key
    and value.

    Key lookup is efficient because the hash function leads directly to a
    bucket with very few keys (often just one)

    What would happen if the proxy changed after storing a key?

    Hashability requires immutability

    Key lookup is very efficient

    Same average time regardless of size


.. nextslide:: Dictionary indexing


Note: Python name look-ups are implemented with dict -- it's highly optimized

.. rst-class:: build
.. container::

    Key to value:

    * lookup is one way

    Value to key:

    * requires visiting the whole dict

    If you need to check dict values often, create another dict or set

    (up to you to keep them in sync)


Dictionary Ordering (not)
-------------------------

Dictionaries have no defined order

.. code-block:: ipython

    In [352]: d = {'one':1, 'two':2, 'three':3}
    In [353]: d
    Out[353]: {'one': 1, 'three': 3, 'two': 2}
    In [354]: d.keys()
    Out[354]: ['three', 'two', 'one']

.. rst-class:: build
.. container::

    You will be fooled by what you see into thinking that the order of pairs
    can be relied on.

    It cannot.

Dictionary Iterating
--------------------

``for``  iterates over the keys

.. code-block:: ipython

    In [15]: d = {'name': 'Brian', 'score': 42}

    In [16]: for x in d:
       ....:     print(x)
       ....:
    score
    name


(note the different order...)

dict keys and values
--------------------

.. code-block:: ipython

    In [20]: d = {'name': 'Brian', 'score': 42}

    In [21]: d.keys()
    Out[21]: ['score', 'name']

    In [22]: d.values()
    Out[22]: [42, 'Brian']

    In [23]: d.items()
    Out[23]: [('score', 42), ('name', 'Brian')]


dict keys and values
--------------------

Iterating on everything

.. code-block:: ipython

    In [26]: d = {'name': 'Brian', 'score': 42}

    In [27]: for k, v in d.items():
       ....:     print("%s: %s" % (k,v))
       ....:
    score: 42
    name: Brian


Dictionary Performance
-----------------------

* indexing is fast and constant time: O(1)

* Membership (``x in s``) constant time: O(1)

* visiting all is proportional to n: O(n)

* inserting is constant time: O(1)

* deleting is constant time: O(1)

http://wiki.python.org/moin/TimeComplexity


Other dict operations:
----------------------

See them all here:

https://docs.python.org/2/library/stdtypes.html#mapping-types-dict

Is it in there?

.. code-block:: ipython

    In [5]: d
    Out[5]: {'that': 7, 'this': 5}

    In [6]: 'that' in d
    Out[6]: True

    In [7]: 'this' not in d
    Out[7]: False

Membership is on the keys.

.. nextslide:: Getting Something

(like indexing)

.. code-block:: ipython

    In [9]: d.get('this')
    Out[9]: 5

.. rst-class:: build
.. container::

    But you can specify a default

    .. code-block:: ipython

        In [11]: d.get(u'something', u'a default')
        Out[11]: u'a default'

    Never raises an Exception (default default is None)

.. nextslide:: Iterating

.. code-block:: ipython

  In [13]: for item in d.iteritems():
     ....:     print item
     ....:
  ('this', 5)
  ('that', 7)
  In [15]: for key in d.iterkeys():
     ....:     print key
     ....:
  this
  that
  In [16]: for val in d.itervalues():
     ....:     print val
     ....:
  5
  7

the ``iter*`` methods *don't actually create the lists*.

.. nextslide:: Popping

gets the value at a given key while removing it

.. rst-class:: build
.. container::

    Pop just a key

    .. code-block:: ipython

        In [19]: d.pop('this')
        Out[19]: 5
        In [20]: d
        Out[20]: {'that': 7}

    pop out an arbitrary key, value pair

    .. code-block:: ipython

        In [23]: d.popitem()
        Out[23]: ('that', 7)
        In [24]: d
        Out[24]: {}

.. nextslide:: Handy Method

``setdefault(key[, default])``

gets the value if it's there, sets it if it's not

.. code-block:: ipython

    In [26]: d = {}

    In [27]: d.setdefault(u'something', u'a value')
    Out[27]: u'a value'
    In [28]: d
    Out[28]: {u'something': u'a value'}
    In [29]: d.setdefault(u'something', u'a different value')
    Out[29]: u'a value'
    In [30]: d
    Out[30]: {u'something': u'a value'}

.. nextslide::

dict View objects:

Like ``keys()``, ``values()``, ``items()``, but maintain a link to the original dict

.. code-block:: ipython

  In [47]: d
  Out[47]: {u'something': u'a value'}
  In [48]: item_view = d.viewitems()
  In [49]: item_view
  Out[49]: dict_items([(u'something', u'a value')])
  In [50]: d['something else'] = u'another value'

  In [51]: item_view
  Out[51]: dict_items([('something else', u'another value'), (u'something', u'a value')])

Cheeseburger Therapy
====================

Four new sessions were requested on Monday and Tuesday night.

Unfortunately, we couldn't respond in time!

If you'd still like to try it out, please start a new
session tonight from 9-10pm.

Homeworks, due Next Monday
==========================

HW 11: Mailroom Madness
HW 12: Dictionaries and Files
HW 13: Trigrams
