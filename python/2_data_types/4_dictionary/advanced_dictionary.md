# Advanced Python Dictionaries -- Notes and Examples

This document summarizes **Advanced Dictionary Concepts in Python**
including:

-   Dictionary Comprehensions
-   Iterating through dictionaries
-   Keys, Values, and Items methods

------------------------------------------------------------------------

# 1. Creating a Dictionary

Basic syntax:

``` python
d = {"k1":1, "k2":2}
print(d)
```

Output

    {'k1': 1, 'k2': 2}

------------------------------------------------------------------------

# 2. Dictionary Comprehension

Just like **list comprehensions**, Python supports **dictionary
comprehensions**.

Syntax

    {key:value for item in iterable}

Example

``` python
d = {x: x**2 for x in range(10)}
print(d)
```

Output

    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

Explanation

-   Keys = `x`
-   Values = `x²`

------------------------------------------------------------------------

# 3. Dictionary Comprehension using zip()

Sometimes keys and values come from **different sources**.

We can use **zip()**.

Example

``` python
keys = ["a","b"]
values = range(2)

d = {k:v**2 for k,v in zip(keys,values)}
print(d)
```

Output

    {'a': 0, 'b': 1}

Explanation

  Key   Value
  ----- -------
  a     0²
  b     1²

------------------------------------------------------------------------

# 4. Iterating Through Dictionary Items

Example dictionary

``` python
d = {"k1":1,"k2":2}
```

Iterating over **items**

``` python
for k,v in d.items():
    print(k,v)
```

Output

    k1 1
    k2 2

Explanation

-   `.items()` returns **key-value pairs**.

------------------------------------------------------------------------

# 5. Iterating Through Keys

``` python
for k in d.keys():
    print(k)
```

Output

    k1
    k2

Explanation

-   `.keys()` returns **only keys**.

------------------------------------------------------------------------

# 6. Iterating Through Values

``` python
for v in d.values():
    print(v)
```

Output

    1
    2

Explanation

-   `.values()` returns **only values**.

------------------------------------------------------------------------

# 7. Dictionary View Methods

These methods provide a **dynamic view of dictionary contents**.

``` python
d = {"k1":1,"k2":2}

print(d.items())
print(d.keys())
print(d.values())
```

Output

    dict_items([('k1', 1), ('k2', 2)])
    dict_keys(['k1', 'k2'])
    dict_values([1, 2])

Important

These are **view objects**, not lists.

------------------------------------------------------------------------

# 8. Python 2 vs Python 3 Iteration

Python 2 had methods like:

    iteritems()
    iterkeys()
    itervalues()

Example

``` python
for k,v in d.iteritems():
    print(k,v)
```

In **Python 3**, these were replaced with:

    items()
    keys()
    values()

which already behave like iterators.

------------------------------------------------------------------------

# 9. Large Dictionary Warning

Be careful with:

    d.items()
    d.keys()
    d.values()

If the dictionary is **very large**, printing them may produce a **huge
output**.

------------------------------------------------------------------------

# 10. Summary Table

  Method               Description
  -------------------- ----------------------------------
  dict comprehension   Creates dictionaries efficiently
  zip()                Combines multiple iterables
  items()              Returns key-value pairs
  keys()               Returns keys
  values()             Returns values

------------------------------------------------------------------------

# 11. Example -- Practical Use

Creating dictionary of numbers and cubes

``` python
cube_dict = {x:x**3 for x in range(5)}
print(cube_dict)
```

Output

    {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

------------------------------------------------------------------------

# 12. Key Takeaways

Important points

Dictionary comprehension

    {x:x**2 for x in range(10)}

Iterating dictionary

    for k,v in d.items()

Getting keys

    d.keys()

Getting values

    d.values()

Getting both

    d.items()

------------------------------------------------------------------------
