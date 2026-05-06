# Lambda Functions

In Python, **lambda functions** are **small anonymous functions** written in a single line using the `lambda` keyword. They are useful when you need a **short function for a short time**, often with functions like `map()`, `filter()`, and `sorted()`.

**Syntax**

```python
lambda arguments : expression
```

---

# 1. Basic Lambda Example

```python
# Normal function
def add(a, b):
    return a + b

print(add(5, 3))

# Lambda function
add_lambda = lambda a, b: a + b
print(add_lambda(5, 3))
```

Output

```
8
8
```

---

# 2. Lambda with `map()`

Used to apply a function to every element.

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))

print(squares)
```

Output

```
[1, 4, 9, 16, 25]
```

---

# 3. Lambda with `filter()`

Used to filter elements.

```python
numbers = [1,2,3,4,5,6,7,8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

Output

```
[2, 4, 6, 8]
```

---

# 4. Lambda with `sorted()`

Useful for sorting complex structures.

```python
students = [
    ("Rahul", 85),
    ("Amit", 70),
    ("Priya", 92)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
```

Output

```
[('Amit', 70), ('Rahul', 85), ('Priya', 92)]
```

---

# 5. Lambda with `max()`

Find maximum using condition.

```python
numbers = [5, 9, 2, 8, 1]

max_num = max(numbers, key=lambda x: x)

print(max_num)
```

Output

```
9
```

---

# 6. Lambda inside another function

```python
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)

print(double(10))
```

Output

```
20
```

---

# 7. Lambda with multiple arguments

```python
multiply = lambda a, b, c: a * b * c

print(multiply(2,3,4))
```

Output

```
24
```

---

# 8. Lambda in list comprehension style usage

```python
numbers = [1,2,3,4,5]

result = [(lambda x: x+10)(x) for x in numbers]

print(result)
```

Output

```
[11, 12, 13, 14, 15]
```

---

💡 **When to use lambda**

* Short one-line functions
* Temporary functions
* With `map()`, `filter()`, `sorted()`, `min()`, `max()`

❌ **Avoid when**

* Logic is complex
* Multiple statements are required

---

If you want, I can also show you **10 Python interview-style lambda problems** (very useful for automation QA interviews).
