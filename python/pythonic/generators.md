# 1. What is a Generator?

A **generator** is a special type of function that:

-   Returns values **one at a time**
-   Uses the **yield** keyword
-   **Pauses execution** and resumes later
-   Does **not store the entire result in memory**

Generators are very useful when working with **large sequences of
data**.

------------------------------------------------------------------------

# 2. Normal Function Example (Creating Cubes)

Normal functions usually store results in memory.

``` python
def create_cubes(n):

    result = []

    for x in range(n):
        result.append(x**3)

    return result

print(create_cubes(10))
```

Output:

    [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

Problem:

-   The **entire list is stored in memory**.

------------------------------------------------------------------------

# 3. Generator Version Using yield

Instead of storing values in a list, we **generate them one by one**.

``` python
def create_cubes(n):

    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)
```

Output:

    0
    1
    8
    27
    64
    125
    216
    343
    512
    729

Advantages:

-   Much **more memory efficient**
-   Values are produced **only when needed**

------------------------------------------------------------------------

# 4. Generator Object

Calling a generator function does not return values immediately.

``` python
create_cubes(10)
```

Output:

    <generator object create_cubes at 0x...>

To convert it to a list:

``` python
list(create_cubes(10))
```

Output:

    [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

------------------------------------------------------------------------

# 5. Fibonacci Generator Example

A Fibonacci sequence:

    1, 1, 2, 3, 5, 8, 13, ...

Generator implementation:

``` python
def gen_fibonacci(n):

    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


for number in gen_fibonacci(10):
    print(number)
```

Output:

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55

This generator only produces the next value when requested.

------------------------------------------------------------------------

# 6. Normal Fibonacci Function (Less Efficient)

``` python
def gen_fibonacci(n):

    output = []

    a = 1
    b = 1

    for i in range(n):
        output.append(a)
        a, b = b, a + b

    return output

print(gen_fibonacci(10))
```

Output:

    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

Problem:

-   Stores **entire list in memory**.

------------------------------------------------------------------------

# 7. next() Function

The **next()** function retrieves the next value from a generator.

Example generator:

``` python
def simple_gen():
    for x in range(3):
        yield x
```

Create generator object:

``` python
g = simple_gen()
```

Use next():

``` python
print(next(g))
print(next(g))
print(next(g))
```

Output:

    0
    1
    2

If we call next again:

``` python
next(g)
```

Output:

    StopIteration

Meaning:

The generator has no more values.

------------------------------------------------------------------------

# 8. Why For Loops Don't Show StopIteration

Example:

``` python
for num in simple_gen():
    print(num)
```

Output:

    0
    1
    2

Explanation:

A **for loop automatically handles StopIteration** internally.

------------------------------------------------------------------------

# 9. Iterable vs Iterator

Example string:

``` python
s = "hello"

for letter in s:
    print(letter)
```

Output:

    h
    e
    l
    l
    o

But calling next directly:

``` python
next(s)
```

Output:

    TypeError: 'str' object is not an iterator

------------------------------------------------------------------------

# 10. Using iter() Function

We convert an iterable into an iterator using **iter()**.

``` python
s = "hello"

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
```

Output:

    h
    e
    l

Now we can use **next()**.

------------------------------------------------------------------------

# 11. Key Concepts

  Concept         Meaning
  --------------- --------------------------------------
  Generator       Function that produces values lazily
  yield           Returns a value and pauses execution
  next()          Gets next value from generator
  iter()          Converts iterable into iterator
  StopIteration   Raised when generator finishes

------------------------------------------------------------------------

# 12. Key Takeaway

The most important concept is:

    yield

Generators:

-   Produce values **on demand**
-   Are **memory efficient**
-   Are commonly used for **large data streams**.

Examples include:

-   `range()`
-   File streaming
-   Data pipelines
-   Machine learning datasets

------------------------------------------------------------------------
