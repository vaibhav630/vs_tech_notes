# Python Object-Oriented Programming (OOP) -- Introduction

This document summarizes the **Introduction to Object-Oriented
Programming (OOP)** in Python.

Topics covered:

-   What is OOP
-   Classes and objects
-   Attributes and methods
-   The `__init__` constructor
-   The `self` keyword

------------------------------------------------------------------------

# 1. What is Object-Oriented Programming (OOP)?

Object-Oriented Programming allows programmers to:

-   Create **custom objects**
-   Define **attributes (data)** for objects
-   Define **methods (functions)** that belong to objects

OOP helps make code:

-   **Organized**
-   **Reusable**
-   **Scalable**

It becomes especially useful when working with **large programs or
libraries**.

------------------------------------------------------------------------

# 2. Built-in Python Objects

Python already has many built-in objects.

Examples:

  Object       Example
  ------------ -----------
  List         `[1,2,3]`
  String       `"hello"`
  Dictionary   `{"a":1}`
  Tuple        `(1,2)`

These objects have **methods**.

Example:

``` python
my_list = [1,2,3]
my_list.append(4)

print(my_list)
```

Output

    [1, 2, 3, 4]

Here:

-   `append()` is a **method**
-   It modifies the **list object**.

------------------------------------------------------------------------

# 3. Why Use OOP?

Functions alone may not be enough when programs grow larger.

OOP helps by:

-   Grouping **data and functions together**
-   Creating **reusable objects**
-   Making code easier to maintain

Example situations:

-   User accounts
-   Bank systems
-   Game characters
-   Data models

------------------------------------------------------------------------

# 4. Defining a Class

Classes are created using the `class` keyword.

Example

``` python
class MyClass:
    pass
```

Explanation

-   `class` → keyword used to define a class
-   `MyClass` → name of the class

Class names usually follow **CamelCase convention**.

Example

    Car
    BankAccount
    StudentRecord

------------------------------------------------------------------------

# 5. The **init** Method (Constructor)

The `__init__` method is called **when an object is created**.

Example

``` python
class Dog:

    def __init__(self, name):
        self.name = name
```

Explanation

-   `__init__` initializes the object
-   `self.name` stores the value inside the object

------------------------------------------------------------------------

# 6. Creating an Object

Example

``` python
class Dog:

    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")

print(my_dog.name)
```

Output

    Buddy

Explanation

-   `Dog("Buddy")` creates an object
-   `"Buddy"` is passed to the constructor
-   It becomes the attribute `name`.

------------------------------------------------------------------------

# 7. Attributes

Attributes are **variables stored inside objects**.

Example

``` python
class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
```

Creating an object

``` python
my_car = Car("Toyota", 2020)

print(my_car.brand)
print(my_car.year)
```

Output

    Toyota
    2020

------------------------------------------------------------------------

# 8. Methods

Methods are **functions that belong to a class**.

Example

``` python
class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says woof!")
```

Using the method

``` python
dog1 = Dog("Buddy")
dog1.bark()
```

Output

    Buddy says woof!

------------------------------------------------------------------------

# 9. The self Keyword

`self` refers to the **current object instance**.

It allows the object to:

-   Access its attributes
-   Call its own methods

Example

``` python
class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello my name is", self.name)
```

Usage

``` python
p = Person("John")
p.greet()
```

Output

    Hello my name is John

------------------------------------------------------------------------

# 10. Structure of a Class

General structure

    class ClassName:

        def __init__(self, parameters):
            self.attribute = parameters

        def method(self):
            # code here

------------------------------------------------------------------------

# 11. Example -- Complete Class

``` python
class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(self.name, "has grade", self.grade)


s1 = Student("Alice", "A")
s1.display()
```

Output

    Alice has grade A

------------------------------------------------------------------------

# 12. Key Concepts & Takeaways

  - Class       Blueprint for objects
  - Object      Instance of a class
  - Attribute   Variable inside object
  - Method      Function inside class
  - **init**    Constructor
  - self        Refers to current object

------------------------------------------------------------------------
