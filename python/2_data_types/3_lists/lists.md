# Lists in Python

## Creating a List

```python
my_list = [1, 2, 3]
emp_list = []
````

---

# Properties of Lists

## Ordered

Lists maintain the **order of elements**.

Example:

```python
my_list = [1, 2, 3]
```

---

## Indexing

You can access elements using **index positions**.

```python
my_list[1]
```

Output

```
2
```

---

## Slicing

You can retrieve multiple elements using **slicing**.

Syntax:

```python
list[start : end : step]
```

Example:

```python
my_list[0::2]
```

Output

```
[0,2]
```

---

## Concatenation

Two lists can be **combined using `+`**.

```python
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]

my_list1 + my_list2
```

Output

```
[1, 2, 3, 4, 5, 6]
```

---

## Number of Elements

Use `len()` to find the **length of a list**.

```python
len(my_list)
```

Output

```
3
```

---

# Mutability

Lists are **mutable**, meaning their elements can be modified after creation.

Example:

```python
my_list[0] = 10
```

---

# Commonly Used List Functions

```python
my_list = [1, 2, 3, 4]
```

| Function                        | Description                                 |
|---------------------------------|---------------------------------------------|
| `my_list.pop()`                 | Removes last element                        |
| `my_list.pop(index)`            | Removes element at given index              |
| `my_list.append('new element')` | Adds element to end of list                 |
| `my_list.sort()`                | Sorts list in ascending order               |
| `my_list.reverse()`             | Reverses the list                           |
| `min(my_list)`                  | Returns smallest element                    |
| `max(my_list)`                  | Returns largest element                     |
| `my_list.count(element)`        | Returns count of given element              |
| `my_list.index(element)`        | Returns index at first occurance of element |

---

# Example

```python
my_list = [4, 1, 3, 2]

my_list.append(5)
my_list.sort()
print(my_list)

print(min(my_list))
print(max(my_list))
```
