
Introduction to Python
======================

This set of course notes involves a mixture of theory and numerical examples demonstrated in Python.
All examples, tutorials and project code will be provided in Python.

If you have never used Python before, I recommend that you use a Python IDE. This will help with organizing, running, and debugging your code.
There are several Python IDEs that are available. I recoomend PyCharm, which can be downloaded here: https://www.jetbrains.com/pycharm/

One of the key advantages of Python is that it has many useful packages that can be easily installed.
There are three critical ones that we'll use a lot in the course: NumPy, SciPy and matplotlib.

* NumPy is a package for fast, multi-dimensional arrays and matrices
* SciPy is a package for scientific computing
* matplotlib is a package for scientific visualization

In PyCharm, you can install and manage the packages in the ``Python Packages`` tab at the bottom of the window.
Search for the package and install each one if you don't have it installed already.
You can also install packages using a package manager, like ``pip`` or ``conda``.

A complete description on how to use PyCharm is located here: https://www.jetbrains.com/help/pycharm/quick-start-guide.html

For more generic information about Python, start here: https://www.python.org/about/gettingstarted/

Python basics
-------------

Python is an interpreted language, meaning that it is not compiled in advance.
These notes use Python 3 exclusively.
What you write in the file, gets interpreted and run on the command line.

* In Python you don't need to declare a variable before using it (Python is implicitly typed)
* The ``print`` function is built-in and very useful

::

  >>> a = 2
  >>> a += 2
  >>> a *= 4
  >>> a -= 2
  >>> print(a)
  14

* String manipulation is straight forward, you can concatenate strings using ``+``

::

  >>> a = 'Hello'
  >>> b = a + ' World!'
  >>> print(b)
  Hello World!

* You can format an output string, using the ``format`` command. This is helpful for controlling how floating point numbers are printed.

::

  >>> pi = 3.141592653589793
  >>> print('{}'.format(pi))
  3.141592653589793
  >>> print('{:.3f}'.format(pi))
  3.142

* Output can be formatted in very sophisticated ways. See this page for many more details: https://docs.python.org/3/library/string.html
* Loops can be made using the ``range`` keyword. The function ``range`` can take one, two or three arguments ``range(stop)`` executes a loop terminating at the index ``stop-1``. With two or three arguments, ``range`` starts from the provided index, and stops on the next to last index with ``step`` taken as the increment to the loop counter.

::

  >>> for i in range(5):
  ...     print(i)
  ...
  0
  1
  2
  3
  4

::

  >>> start = 2
  >>> end = 6
  >>> for i in range(start, end):
  ...     print(i)
  ...
  2
  3
  4
  5

::

  >>> for i in range(2, 8, 2):
  ...     print(i)
  ...
  2
  4
  6

* Logical conditions are straightforward in Python.

::

  >>> a = 1
  >>> b = 2
  >>> c = 3
  >>> if a == b:
  ...     print('a == b')
  ... elif a == c:
  ...     print('a == c')
  ... else:
  ...     print('a != b and b != c')
  ...
  a != b and b != c

* Python also has some built-in data types like lists and dictionaries that are helpful.

::

  >>> if a >= b:
  ...     print('a >= b')
  ... elif a <= c:
  ...     print('a <= c')
  ... else:
  ...     print('!(a >= b and a <= c)')
  ...
  a <= c

* Boolean logic in python uses the keywords ``and`` and ``or``:

::

  >>> a = False
  >>> b = True
  >>> print(a and b)
  False
  >>> print(a and not b)
  False
  >>> print(not a and b)
  True
  >>> print(a or b)
  True

* Python also implements some handy data structures that can be useful. Lists of objects take the form

::

  >>> a = [1, 2, 3, 4]
  >>> a.append('Nocedal')
  >>> a.extend(['Wright', 'Mangasarian'])
  >>> print(a)
  [1, 2, 3, 4, 'Nocedal', 'Wright', 'Mangasarian']
  >>> for obj in a:
  ...     print(obj)
  ...
  1
  2
  3
  4
  Nocedal
  Wright
  Mangasarian
  >>> for index, obj in enumerate(a):
  ...     print(index, obj)
  ...
  0 1
  1 2
  2 3
  3 4
  4 Nocedal
  5 Wright
  6 Mangasarian

* Functions can be defined in python as follows

::

  >>> def isThisFletcher(s, default='conjugate'):
  ...     if s == 'Fletcher':
  ...             return True
  ...     return False
  ...
  >>> isThisFletcher('Fletcher')
  True
  >>> isThisFletcher('Reeves')
  False

* Note that variables that are global or local (including the arguments to the function) can be accessed within the function.
* I strongly recommend that you *do not* use global variables. Pass variables as arguments. Do not use global variables!
* If there is a global variable and a local variable with the same name, the local variable is used. But it can be confusing if you rely on this!

There are a lot of additional things we'll do with python. There are many examples in these notes.

* A quick summary of some Python features: https://www.stavros.io/tutorials/python/
* A detailed and thorough introduction to Python 3: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/


NumPy basics
------------

NumPy is a powerful package that implements multi-dimensional arrays in Python.

* To use any NumPy features in Python, you have to first import the package.

::

  >>> import numpy as np

* NumPy uses arrays that can either be generated directly or be created from Python lists

::

  >>> apy = [0, 1, 2, 5, 10, 10]
  >>> a = np.array(apy)
  >>> print(a)
  [ 0  1  2  5 10 10]
  >>> print(a.dtype)
  int64

* Be careful of the data type. Sometimes you might create a NumPy array of integers when you wanted floats!
* There are two ways around this, either declare the type directly or make sure to initialize the list as a float.

::

  >>> apy = [0, 1, 2, 5, 10, 10]
  >>> a = np.array(apy, dtype=float)
  >>> print(a)
  [ 0.  1.  2.  5. 10. 10.]
  >>> print(a.dtype)
  float64

* 2 dimensional (and higher-dimensional) arrays can also be created from lists of lists as long as they're the right length

::

  >>> apy = [[1, 2, 3], [3, 4, 5]]
  >>> a = np.array(apy)
  >>> print(a)
  array([[1, 2, 3],
        [3, 4, 5]])
  >>> print(a.shape)
  (2, 3)

* You can create NumPy arrays directly as well. The default data type is a float.

::

  >>> a = np.zeros(4)
  >>> print(a)
  [0. 0. 0. 0.]
  >>> a = np.zeros((4, 5))
  >>> print(a)
  [[0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0.]]
  >>> print(a.shape)
  (4, 5)

* There are many ways to index into arrays. Indexing is zero-based so you can do the following

::

  >>> a = np.zeros((5, 6))
  >>> for i in range(5):
  ...     for j in range(6):
  ...             a[i, j] = i + j
  ...
  >>> print(a)
  [[0. 1. 2. 3. 4. 5.]
  [1. 2. 3. 4. 5. 6.]
  [2. 3. 4. 5. 6. 7.]
  [3. 4. 5. 6. 7. 8.]
  [4. 5. 6. 7. 8. 9.]]

* You can assign slices of values to arrays

For more details on how to use NumPy, please read this document: https://numpy.org/doc/stable/user/absolute_beginners.html

matplotlib basics
-----------------

Matplotlib is a package for scientific visualization in Python.
For a thorough introduction to matplotlib, see this link: https://matplotlib.org/stable/tutorials/introductory/pyplot.html