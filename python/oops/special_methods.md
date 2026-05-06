# Python OOP -- Special Methods (Magic / Dunder Methods)

This document explains **Special Methods in Python OOP**, sometimes
called:

-   Magic Methods
-   Dunder Methods (Double underscore methods)

These methods allow **built‑in Python functions** like `print()`,
`len()`, and `del` to work with **user‑defined objects**.

------------------------------------------------------------------------

# 1. Why Special Methods Exist

Built‑in Python objects already support many operations.

Example with a list:

``` python
mylist = [1,2,3]

print(len(mylist))
```

Output

    3

But if we create our own object:

``` python
class Sample:
    pass

mysample = Sample()

len(mysample)
```

Output

    TypeError: object of type 'Sample' has no len()

Python doesn't know how to calculate the length of this object.

This is where **special methods** help.

------------------------------------------------------------------------

# 2. Example Class -- Book

Let's create a `Book` class.

``` python
class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages
```

Creating an instance:

``` python
b = Book("Python Rocks", "Jose", 200)
```

------------------------------------------------------------------------

# 3. Printing an Object

If we try to print the object:

``` python
print(b)
```

Output

    <__main__.Book object at 0x...>

Python prints the **memory location** instead of useful information.

------------------------------------------------------------------------

# 4. The **str** Method

The `__str__` method defines the **string representation** of an object.

Example:

``` python
class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
```

Usage:

``` python
b = Book("Python Rocks", "Jose", 200)

print(b)
```

Output

    Python Rocks by Jose

Explanation:

`print()` internally calls the object's ****str**()** method.

------------------------------------------------------------------------

# 5. The **len** Method

This method allows the `len()` function to work with your object.

Example:

``` python
class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages
```

Usage:

``` python
b = Book("Python Rocks", "Jose", 200)

print(len(b))
```

Output

    200

Explanation:

`len()` calls the object's ****len**()** method.

------------------------------------------------------------------------

# 6. The **del** Method

The `__del__` method runs when an object is **deleted from memory**.

Example:

``` python
class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __del__(self):
        print("A book object has been deleted")
```

Usage:

``` python
b = Book("Python Rocks", "Jose", 200)

del b
```

Output

    A book object has been deleted

------------------------------------------------------------------------

# 7. Complete Example

``` python
class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book deleted")


b = Book("Python Rocks", "Jose", 200)

print(b)
print(len(b))

del b
```

Output

    Python Rocks by Jose
    200
    Book deleted

------------------------------------------------------------------------

# 8. Why These Methods Are Useful

They allow **user-defined objects to behave like built-in Python objects**.

Example operations enabled:

-  print(object) : **str**
-  len(object)   : **len**
-  del object    : **del**

------------------------------------------------------------------------

# 9. Naming of Special Methods

They use **double underscores** on both sides.
That's why they are called **dunder methods**.

------------------------------------------------------------------------

# 10. Key Takeaways

Special methods allow Python to integrate your objects with built‑in functionality.

Most commonly used:

    __init__  -> constructor
    __str__   -> string representation
    __len__   -> object length
    __del__   -> object deletion behavior

These methods make your objects:

-   More readable
-   More Pythonic
-   Compatible with built-in functions
