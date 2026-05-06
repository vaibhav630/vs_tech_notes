# Common Python Built-in Functions for Lists

This document covers commonly used Python functions used with lists and other iterables.

---

# 1. count()

Returns the **number of occurrences of a value** in a list.

### Syntax

```python
list.count(value)
````

### Example

```python
numbers = [5, 2, 5, 3, 5, 4]

print(numbers.count(5))
```

Output

```
3
```

---

# 2. index()

Returns the **index of the first occurrence** of a value.

### Syntax

```python
list.index(value)
```

### Example

```python
numbers = [10, 20, 30, 40]

print(numbers.index(30))
```

Output

```
2
```

⚠️ Note:
If the element is not present, Python raises **ValueError**.

---

# 3. sum()

Returns the **sum of all elements** in an iterable.

### Syntax

```python
sum(iterable)
```

### Example

```python
numbers = [10, 20, 30, 40]

print(sum(numbers))
```

Output

```
100
```

---

# 4. max()

Returns the **largest element** in a list.

### Syntax

```python
max(iterable)
```

### Example

```python
numbers = [2, 5, 9, 7, 6, 8]

print(max(numbers))
```

Output

```
9
```

---

# 5. min()

Returns the **smallest element** in a list.

### Syntax

```python
min(iterable)
```

### Example

```python
numbers = [2, 5, 9, 7, 6, 8]

print(min(numbers))
```

Output

```
2
```

---

# Other Commonly Used Python Functions

---

# 6. len()

Returns the **number of elements** in a list.

### Example

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output

```
3
```

---

# 7. sorted()

Returns a **new sorted list** without modifying the original list.

### Example

```python
numbers = [4, 1, 3, 2]

print(sorted(numbers))
```

Output

```
[1, 2, 3, 4]
```

---

# 8. list.sort()

Sorts the list **in place**.

### Example

```python
numbers = [4, 1, 3, 2]

numbers.sort()

print(numbers)
```

Output

```
[1, 2, 3, 4]
```

---

# 9. reversed()

Returns a **reverse iterator**.

### Example

```python
numbers = [1, 2, 3, 4]

print(list(reversed(numbers)))
```

Output

```
[4, 3, 2, 1]
```

---

# 10. any()

Returns **True if at least one element is True**.

### Example

```python
numbers = [0, 0, 3, 0]

print(any(numbers))
```

Output

```
True
```

---

# 11. all()

Returns **True if all elements are True**.

### Example

```python
numbers = [1, 2, 3]

print(all(numbers))
```

Output

```
True
```

---

# 12. enumerate()

Returns **index and value pairs**.

### Example

```python
numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)
```

Output

```
0 10
1 20
2 30
```

---

# Quick Summary

| Function      | Purpose                       |
| ------------- | ----------------------------- |
| `count()`     | Count occurrences             |
| `index()`     | Find index of element         |
| `sum()`       | Sum of elements               |
| `max()`       | Largest element               |
| `min()`       | Smallest element              |
| `len()`       | Length of list                |
| `sorted()`    | Return sorted list            |
| `sort()`      | Sort list in place            |
| `reversed()`  | Reverse iterable              |
| `any()`       | True if any element is true   |
| `all()`       | True if all elements are true |
| `enumerate()` | Get index + value pairs       |

```

✅ These are the **most commonly used functions with lists in Python**.

If you'd like, I can also give you a **much more powerful `.md` cheat sheet covering the 25 most useful Python built-in functions developers use daily**.
```
