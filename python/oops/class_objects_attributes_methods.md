# Python OOP -- Classes and Attributes

This document explains **Object-Oriented Programming in Python (Part
1)** focusing on:

-   The `class` keyword
-   Creating objects (instances)
-   The `__init__` constructor
-   Attributes
-   The `self` keyword

------------------------------------------------------------------------

# 1. Objects in Python

Everything in Python is an **object**.

Example:

``` python
mylist = [1,2,3]
print(type(mylist))
```

Output

    <class 'list'>

Another example:

``` python
myset = set()
print(type(myset))
```

Output

    <class 'set'>

Built‑in objects such as lists and sets already have **methods and
attributes**.

Example:

``` python
mylist.append(4)
print(mylist)
```

Output

    [1, 2, 3, 4]

------------------------------------------------------------------------

# 2. Creating Your Own Class

Classes allow us to create **user-defined objects**.

Basic syntax:

``` python
class Sample:
    pass
```

Explanation:

-   `class` → keyword to define a class
-   `Sample` → name of the class
-   `pass` → placeholder when no code exists yet

------------------------------------------------------------------------

# 3. Creating an Instance (Object)

We create objects from a class like this:

``` python
class Sample:
    pass

my_sample = Sample()

print(type(my_sample))
```

Output

    <class '__main__.Sample'>

Here:

-   `Sample()` creates an **instance** of the class.

------------------------------------------------------------------------

# 4. Class Naming Convention

Class names follow **CamelCase**.

Examples:

    Dog
    BankAccount
    StudentRecord
    CarEngine

Variables and functions usually use **snake_case**.

------------------------------------------------------------------------

# 5. Adding Attributes Using **init**

The `__init__` method is a **constructor**.

It runs automatically when an object is created.

Example:

``` python
class Dog:

    def __init__(self, breed):
        self.breed = breed
```

------------------------------------------------------------------------

# 6. Creating an Object with Attributes

``` python
class Dog:

    def __init__(self, breed):
        self.breed = breed


my_dog = Dog("Labrador")

print(my_dog.breed)
```

Output

    Labrador

Explanation:

-   `"Labrador"` is passed as the argument
-   It becomes the attribute `breed`.

------------------------------------------------------------------------

# 7. Understanding self

`self` refers to the **current instance of the object**.

Example:

    self.breed = breed

Meaning:

    attribute = parameter

So:

    my_dog.breed = "Labrador"

------------------------------------------------------------------------

# 8. Parameter vs Attribute

Example:

``` python
class Dog:

    def __init__(self, mybreed):
        self.breed = mybreed
```

Here:

  Element      Meaning
  ------------ ----------------------------
  mybreed      parameter
  self.breed   attribute stored in object

Usage:

``` python
my_dog = Dog("Husky")
print(my_dog.breed)
```

Output

    Husky

------------------------------------------------------------------------

# 9. Multiple Attributes

We can define multiple attributes.

Example:

``` python
class Dog:

    def __init__(self, breed, name, spots):

        self.breed = breed
        self.name = name
        self.spots = spots
```

------------------------------------------------------------------------

# 10. Creating an Object with Multiple Attributes

``` python
my_dog = Dog("Lab", "Sammy", False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
```

Output

    Lab
    Sammy
    False

------------------------------------------------------------------------

# 11. Expected Data Types

Attributes can be different data types.

Example:

  Attribute   Expected Type
  ----------- ---------------
  - breed       string
  - name        string
  - spots       boolean

Example:

``` python
Dog("Lab", "Sammy", False)
```

Python does **not enforce types automatically**.

Example:

``` python
Dog("Lab","Sammy","no spots")
```

This will still work unless validation is added.

------------------------------------------------------------------------

# 12. Accessing Attributes

Once an object is created, attributes can be accessed using dot
notation.

Example:

``` python
print(my_dog.name)
```

Output

    Sammy

------------------------------------------------------------------------


