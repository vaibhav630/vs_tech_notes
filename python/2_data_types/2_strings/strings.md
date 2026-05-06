# Python Strings Notes

## 1. Strings in Python

Strings can be written using **single quotes** or **double quotes**.

### Examples

```python
'single quote'
"double quote"
"Nested 'single quote'"
'Nested "double quote"'
````

---

# 2. String Indexing

Strings use **index positions** to access characters.

Example string:

```python
my_str = "TABLE"
```

| Character      | T  | A  | B  | L  | E  |
| -------------- | -- | -- | -- | -- | -- |
| Positive Index | 0  | 1  | 2  | 3  | 4  |
| Negative Index | -5 | -4 | -3 | -2 | -1 |

Example:

```python
my_str[0]   # T
my_str[1]   # A
my_str[-1]  # E
```

---

# 3. String Slicing

Syntax:

```python
string[start_index : end_index : step]
```

Important rule:

* **end_index is exclusive** (not included in the result)



---

## 3a. Slicing Examples

Given:

```python
my_str = "abcdefgh"
```

| Expression      | Result   | Meaning             |
| --------------- | -------- | ------------------- |
| `my_str[2:]`    | cdefgh   | From index 2 to end |
| `my_str[0:3]`   | abc      | From index 0 to 2   |
| `my_str[:3]`    | abc      | Start to index 2    |
| `my_str[3:6]`   | def      | Index 3 to 5        |
| `my_str[::]`    | abcdefgh | Full string         |
| `my_str[::3]`   | adg      | Every 3rd character |
| `my_str[2:7:2]` | ceg      | Step of 2           |

## 3b. Practice Examples

Given:

```python
my_str = "abcdefgh"
```

### Grab last letter

```python
print(my_str[-1])
```

Output

```
h
```

### Reverse the string

```python
print(my_str[::-1])
```

Output

```
hgfedcba
```

---

# 4a. String Concatenation

```python
first = "Hello"
second = "World"

print(first + second)
```

Output

```
HelloWorld
```
---

# 4b. String Repetition 

Python allows multiplying a string by an integer to **repeat it multiple times**.

Example:

```python
print("Hi" * 5)
```

Output

```
HiHiHiHiHi
```

### How it Works

* `"Hi"` → string
* `*` → repetition operator
* `5` → number of times the string repeats

Python internally performs:

```
"Hi" + "Hi" + "Hi" + "Hi" + "Hi"
```

---

# 5. String Immutability

Strings **cannot be modified after creation**.

Example:

```python
my_str = "Jello World"
my_str[0] = "H"
```

This will cause an **error** because strings are **immutable**.

Correct way:

```python
my_str = "H" + my_str[1:]
print(my_str)
```

Output

```
Hello World
```

---

# 6. Common String Functions

```python
my_str = "Hello World"
```

| Function     | Description              | Example Output        |
| ------------ | ------------------------ | --------------------- |
| `upper()`    | Convert to uppercase     | HELLO WORLD           |
| `lower()`    | Convert to lowercase     | hello world           |
| `split()`    | Split by space           | ['Hello','World']     |
| `split('o')` | Split using character    | ['Hell', ' W', 'rld'] |
| `count('o')` | Count occurrences        | 2                     |
| `index('l')` | First index of character | 2                     |

Example:

```python
my_str.upper()
my_str.lower()
my_str.split()
my_str.split('o')
my_str.count('o')
my_str.index('l')
```

---

# 7. f-Strings (Formatted Strings)

f-strings allow inserting variables inside strings.

Example:

```python
name = "Vaibhav"
print(f"Hello, My name is {name}")
```

Output

```
Hello, My name is Vaibhav
```

---

# 8. String Interpolation