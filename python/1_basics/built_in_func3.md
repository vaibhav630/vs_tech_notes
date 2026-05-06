# common iterables

An **iterable** is any object you can loop over with `for`.

Common iterables:

* **list**
* **tuple**
* **set**
* **string**
* **dictionary**
* **range**
* **generator**

---

# 1. Functions That Work on Any Iterable

These are **general Python built-in functions**.

| Function      | Works On                       |
| ------------- | ------------------------------ |
| `len()`       | list, tuple, set, dict, string |
| `sum()`       | list, tuple, set               |
| `max()`       | list, tuple, set, string       |
| `min()`       | list, tuple, set, string       |
| `sorted()`    | list, tuple, set, string       |
| `any()`       | any iterable                   |
| `all()`       | any iterable                   |
| `enumerate()` | any iterable                   |
| `reversed()`  | sequence types                 |

### Example

```python
print(len("Python"))
```

Output

```
6
```

```python
print(max("Python"))
```

Output

```
y
```

(because `'y'` has the highest ASCII value)

---

# 2. Methods That Work on Some Other Types

### `count()` and `index()`

Work on **sequence types**:

| Type       | Works? |
| ---------- | ------ |
| list       | ✅      |
| tuple      | ✅      |
| string     | ✅      |
| set        | ❌      |
| dictionary | ❌      |

Example:

```python
print("hello".count("l"))
```

Output

```
2
```

---

# Simple Rule to Remember

### Built-in Functions

Work on **many iterables**

```
len()
sum()
max()
min()
sorted()
```

---