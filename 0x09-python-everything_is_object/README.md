In Python, everything is object.

When doing aliasing, changes made to one object are reflected in the other object.
if
>>> a = [1, 2, 3, 4]
>>> b = a
>>> b == a
True
>>> b is a
True

If you want to make changes to a copy of an object and not have the changes reflected on the original object, use the slicing operator.
>>> a = [1, 2, 3, 4]
>>> b = a[:]
>>> b[0] = 12
>>> b
[12, 2, 3, 4]
>>> a
[1, 2, 3, 4]
