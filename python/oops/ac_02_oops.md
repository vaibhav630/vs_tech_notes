# Object-Oriented Programming in Python (Part 2 )

## 🚀 Introduction

This part completes OOP with advanced and practical concepts:

* `del` keyword
* Private attributes & methods
* Inheritance (all types)
* `super()` method
* Class methods vs static vs instance
* Property decorator
* Polymorphism (Operator Overloading)
* Dunder (magic) methods
* Practice problems

---

# 🗑️ `del` Keyword

### 🔹 Purpose

Used to:

* Delete object properties
* Delete entire object

---

### ✅ Example

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shraddha")

del s1
# print(s1)  # ❌ Error
```

**Output:**

```text
NameError: name 's1' is not defined
```

---

### Delete Attribute

```python
s1 = Student("Shraddha")
print(s1.name)

del s1.name
# print(s1.name)  # ❌ Error
```

---

# 🔐 Private Attributes & Methods

### 🔹 Why?

To protect sensitive data (like passwords)

---

### 🔹 Syntax

Use **double underscore (`__`)**

---

### ✅ Example

```python
class Account:
    def __init__(self, acc_no, password):
        self.acc_no = acc_no
        self.__password = password

acc1 = Account(12345, "abcde")

print(acc1.acc_no)
# print(acc1.__password) ❌ Error
```

---

### 🔹 Access Inside Class

```python
class Account:
    def __init__(self, acc_no, password):
        self.acc_no = acc_no
        self.__password = password

    def reset_password(self):
        print(self.__password)

acc1 = Account(12345, "abcde")
acc1.reset_password()
```

**Output:**

```text
abcde
```

---

## 🔒 Private Methods

```python
class Person:
    def __hello(self):
        print("Hello person")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()
```

**Output:**

```text
Hello person
```

---

# 🧬 Inheritance

### 🔹 Definition

Child class inherits properties & methods of parent class.

---

## ✅ Example

```python
class Car:
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")

car1.start()
```

**Output:**

```text
Car started
```

---

## 🔁 Types of Inheritance

### 1. Single Inheritance

One parent → one child

### 2. Multilevel Inheritance

```python
class A:
    varA = "A"

class B(A):
    varB = "B"

class C(B):
    varC = "C"

c1 = C()
print(c1.varA, c1.varB, c1.varC)
```

---

### 3. Multiple Inheritance

```python
class A:
    varA = "A"

class B:
    varB = "B"

class C(A, B):
    varC = "C"

c1 = C()
print(c1.varA, c1.varB)
```

---

# ⚡ `super()` Method

Used to access parent class methods/constructor.

---

### ✅ Example

```python
class Car:
    def __init__(self, type):
        self.type = type

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

car1 = ToyotaCar("Prius", "Electric")
print(car1.type)
```

**Output:**

```text
Electric
```

---

### Call Parent Method

```python
super().start()
```

---

# ⚙️ Types of Methods

| Type            | First Argument | Use Case            |
| --------------- | -------------- | ------------------- |
| Instance Method | `self`         | Object-specific     |
| Class Method    | `cls`          | Class-level changes |
| Static Method   | none           | Utility functions   |

---

## 🧠 Class Method

```python
class Person:
    name = "Anonymous"

    @classmethod
    def change_name(cls, name):
        cls.name = name

Person.change_name("Rahul")
print(Person.name)
```

---

## ⚠️ Important Concept

```python
self.name = name
```

➡️ Creates **instance attribute**

```python
Person.name = name
```

➡️ Changes **class attribute**

---

# 🧾 Property Decorator

### 🔹 Problem

Derived values don’t auto-update

---

### ❌ Without Property

```python
self.percentage = (marks)/3
```

Does NOT update automatically

---

### ✅ With Property

```python
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return (self.phy + self.chem + self.math) / 3

s1 = Student(98, 97, 96)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)
```

**Output:**

```text
97.0
93.0
```

---

# 🎭 Polymorphism

### 🔹 Meaning

Same operator/function → different behavior

---

## 🔹 Operator Overloading

```python
print(1 + 2)            # 3
print("Hi " + "All")    # Concatenation
print([1,2] + [3,4])    # Merge lists
```

---

# ⚡ Dunder Methods (Magic Methods)

Used to define custom operator behavior.

---

## ✅ Example: Custom `+`

```python
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.img + other.img
        )

    def show(self):
        print(f"{self.real} + {self.img}i")

n1 = Complex(1, 3)
n2 = Complex(4, 6)

n3 = n1 + n2
n3.show()
```

**Output:**

```text
5 + 9i
```

---

## ➕ Subtraction

```python
def __sub__(self, other):
    return Complex(
        self.real - other.real,
        self.img - other.img
    )
```

---

# 🧪 Practice Questions

---

## 🟢 1. Circle Class

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)

print(c1.area())
print(c1.perimeter())
```

**Output:**

```text
1386.0
132.0
```

---

## 🟢 2. Employee & Engineer

```python
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print(self.role, self.dept, self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("Engineer", "IT", 75000)
        self.name = name
        self.age = age

e1 = Engineer("Elon", 40)
e1.show_details()
```

---

## 🟢 3. Order Comparison (`>`)

```python
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

o1 = Order("Chips", 20)
o2 = Order("Tea", 15)

print(o1 > o2)
```

**Output:**

```text
True
```

---

# 🎯 Final Takeaways

* `del` → delete object/attributes
* `__private` → restrict access
* Inheritance → reuse code
* `super()` → call parent
* `@classmethod` → modify class data
* `@property` → dynamic attributes
* Polymorphism → multiple behavior
* Dunder methods → customize operators

---
