# Python List Methods -- Detailed Notes

This document summarizes commonly used **Python List Methods** with
examples and outputs.

------------------------------------------------------------------------

# 1. Creating a Simple List

``` python
l = [1,2,3]
print(l)
```

Output

    [1, 2, 3]

------------------------------------------------------------------------

# 2. append()

Adds a single element to the **end of the list**.

``` python
l = [1,2,3]
l.append(4)
print(l)
```

Output

    [1, 2, 3, 4]

Key Point

-   Adds the **entire object** as one element.

------------------------------------------------------------------------

# 3. count()

Counts how many times an element occurs in a list.

``` python
l = [1,2,3]

print(l.count(1))
print(l.count(10))
```

Output

    1
    0

Key Point

-   Returns **0 if element is not present**
-   Does **not raise an error**.

------------------------------------------------------------------------

# 4. append() vs extend()

## Using append()

``` python
x = [1,2,3]
x.append([4,5])
print(x)
```

Output

    [1, 2, 3, [4, 5]]

The **entire list becomes a single element**.

------------------------------------------------------------------------

## Using extend()

``` python
x = [1,2,3]
x.extend([4,5])
print(x)
```

Output

    [1, 2, 3, 4, 5]

Key Difference

  Method   Behavior
  -------- ----------------------------
  append   Adds entire object
  extend   Adds elements individually

------------------------------------------------------------------------

# 5. index()

Returns the **index position** of an element.

``` python
l = [1,2,3,4]
print(l.index(2))
```

Output

    1

If element does not exist

``` python
l.index(10)
```

Output

    ValueError: 10 is not in list

------------------------------------------------------------------------

# 6. insert()

Inserts an element at a specific index.

Syntax

    list.insert(index, element)

Example

``` python
l = [1,2,3,4]
l.insert(2,"inserted")
print(l)
```

Output

    [1, 2, 'inserted', 3, 4]

------------------------------------------------------------------------

# 7. pop()

Removes and returns an element from the list.

Default behavior removes **last element**.

``` python
l = [1,2,3,4]
ele = l.pop()
print(ele)
print(l)
```

Output

    4
    [1, 2, 3]

Removing a specific index

``` python
l = [1,2,3]
l.pop(0)
print(l)
```

Output

    [2, 3]

------------------------------------------------------------------------

# 8. remove()

Removes the **first occurrence of a value**.

``` python
l = [1,2,"inserted",3]
l.remove("inserted")
print(l)
```

Output

    [1, 2, 3]

Example with duplicate values

``` python
l = [1,2,3,4,3]
l.remove(3)
print(l)
```

Output

    [1, 2, 4, 3]

Key Point

-   Only removes the **first occurrence**.

------------------------------------------------------------------------

# 9. reverse()

Reverses the list **in place**.

``` python
l = [1,2,3,4]
l.reverse()
print(l)
```

Output

    [4, 3, 2, 1]

Important

-   Changes the **original list permanently**.

------------------------------------------------------------------------

# 10. sort()

Sorts the list **in place**.

``` python
l = [4,1,3,2]
l.sort()
print(l)
```

Output

    [1, 2, 3, 4]

Key Point

-   Sorts the **original list**
-   Does **not create a new list**.

------------------------------------------------------------------------

# 11. Summary Table

  Method      Description
  ----------- ------------------------------
  append()    Adds element to end
  count()     Counts occurrences
  extend()    Adds elements of iterable
  index()     Returns index of element
  insert()    Inserts element at position
  pop()       Removes element by index
  remove()    Removes first matching value
  reverse()   Reverses list
  sort()      Sorts list

------------------------------------------------------------------------

# 12. Key Takeaways

Important differences to remember

append vs extend

    append([4,5]) -> [1,2,3,[4,5]]
    extend([4,5]) -> [1,2,3,4,5]

remove vs pop

    remove(value) -> removes by value
    pop(index) -> removes by index

sort vs reverse

    sort() -> orders values
    reverse() -> flips order

Both operate **in place**.

------------------------------------------------------------------------
