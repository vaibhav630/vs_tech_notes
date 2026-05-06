# 1. `print()` Function

The `print()` function is used to **display output on the console**.

### Example

```python
print("Hello World")
print(10)
print("Python is easy")
```

### Multiple Values

```python
name = "Vaibhav"
age = 30

print(name, age)
```

---

# 2. `type()` Function

The `type()` function is used to check the **data type of a variable**.

### Example:

```python
a = 10
print(type(a))

b = 5.5
print(type(b))

c = "Python"
print(type(c))
```

---

# 3. `len()` Function

The `len()` function returns the **number of items in an object**.

It works with:

* Strings
* Lists
* Tuples
* Sets
* Dictionaries

### Example

```python
name = "Python"
print(len(name))
```

Output

```
6
```

---

# 4. `input()` Function

The `input()` function allows the user to **enter data from the keyboard**.

By default, the input is stored as a **string**.

### Example

```python
result = input("Enter a number: ")

print(result)
print(float(result))
print(int(result))
```

### Explanation

| Function  | Purpose                          |
| --------- | -------------------------------- |
| `input()` | Takes user input as string       |
| `float()` | Converts input to decimal number |
| `int()`   | Converts input to integer        |

Example Output

```
Enter a number: 25
25
25.0
25
```

---