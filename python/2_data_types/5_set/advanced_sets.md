# Advanced Python Sets -- Notes and Examples

This document summarizes **Advanced Set Methods in Python** including:

-   Adding and removing elements
-   Set operations (difference, intersection, union)
-   Comparison methods
-   Update methods

------------------------------------------------------------------------

# 1. Creating a Set

``` python
s = set()
s.add(1)
s.add(2)
print(s)
```

Output

    {1, 2}

Sets automatically **remove duplicates**.

``` python
s.add(2)
print(s)
```

Output

    {1, 2}

------------------------------------------------------------------------

# 2. clear()

Removes all elements from a set.

``` python
s = {1,2,3}
s.clear()
print(s)
```

Output

    set()

------------------------------------------------------------------------

# 3. copy()

Creates a copy of a set.

``` python
s = {1,2,3}
sc = s.copy()

print(sc)
```

Output

    {1, 2, 3}

Changes in original set do not affect the copy.

``` python
s.add(4)

print(s)
print(sc)
```

Output

    {1, 2, 3, 4}
    {1, 2, 3}

------------------------------------------------------------------------

# 4. difference()

Returns elements present in the **first set but not the second**.

``` python
s1 = {1,2,3,4}
s2 = {1,4,5}

print(s1.difference(s2))
```

Output

    {2, 3}

------------------------------------------------------------------------

# 5. difference_update()

Updates the first set by removing common elements.

``` python
s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)
print(s1)
```

Output

    {2, 3}

------------------------------------------------------------------------

# 6. discard()

Removes an element **if it exists**.

``` python
s = {1,2,3,4}

s.discard(2)
print(s)
```

Output

    {1, 3, 4}

If element doesn't exist:

``` python
s.discard(10)
```

No error occurs.

------------------------------------------------------------------------

# 7. intersection()

Returns elements **common in both sets**.

``` python
s1 = {1,2,3}
s2 = {1,2,4}

print(s1.intersection(s2))
```

Output

    {1, 2}

------------------------------------------------------------------------

# 8. intersection_update()

Updates the set to the **intersection result**.

``` python
s1 = {1,2,3}
s2 = {1,2,4}

s1.intersection_update(s2)
print(s1)
```

Output

    {1, 2}

------------------------------------------------------------------------

# 9. isdisjoint()

Returns **True if sets have no common elements**.

``` python
s1 = {1,2}
s2 = {3,4}

print(s1.isdisjoint(s2))
```

Output

    True

Example with common elements

``` python
s1 = {1,2}
s2 = {1,3}

print(s1.isdisjoint(s2))
```

Output

    False

------------------------------------------------------------------------

# 10. issubset()

Checks if one set is **contained within another**.

``` python
s1 = {1,2}
s2 = {1,2,4}

print(s1.issubset(s2))
```

Output

    True

------------------------------------------------------------------------

# 11. issuperset()

Checks if a set **contains another set**.

``` python
print(s2.issuperset(s1))
```

Output

    True

------------------------------------------------------------------------

# 12. symmetric_difference()

Returns elements present in **only one set**.

``` python
s1 = {1,2}
s2 = {1,2,4}

print(s1.symmetric_difference(s2))
```

Output

    {4}

------------------------------------------------------------------------

# 13. symmetric_difference_update()

Updates the set to keep only **unique elements between sets**.

``` python
s1 = {1,2}
s2 = {1,2,4}

s1.symmetric_difference_update(s2)
print(s1)
```

Output

    {4}

------------------------------------------------------------------------

# 14. union()

Returns elements present in **either set**.

``` python
s1 = {1,2}
s2 = {1,2,4}

print(s1.union(s2))
```

Output

    {1, 2, 4}

------------------------------------------------------------------------

# 15. update()

Updates a set with elements from another set.

``` python
s1 = {1,2}
s2 = {1,2,4}

s1.update(s2)
print(s1)
```

Output

    {1, 2, 4}

------------------------------------------------------------------------

# 16. Summary Table

  Method                          Description
  ------------------------------- ----------------------------------
  add()                           Adds element to set
  clear()                         Removes all elements
  copy()                          Creates copy
  difference()                    Elements only in first set
  difference_update()             Updates first set
  discard()                       Removes element if exists
  intersection()                  Common elements
  intersection_update()           Updates with intersection
  isdisjoint()                    Checks if sets share no elements
  issubset()                      Checks subset
  issuperset()                    Checks superset
  symmetric_difference()          Elements in only one set
  symmetric_difference_update()   Updates symmetric difference
  union()                         Combines sets
  update()                        Updates with union

------------------------------------------------------------------------

# 17. Key Takeaways

Important set operations

    intersection()
    union()
    difference()
    symmetric_difference()

Comparison operations

    issubset()
    issuperset()
    isdisjoint()

Update operations modify the **original set**

    update()
    intersection_update()
    difference_update()
    symmetric_difference_update()

Sets are extremely useful for:

-   Removing duplicates
-   Membership testing
-   Fast comparisons
-   Mathematical set operations
