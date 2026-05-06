# Object-Oriented Programming (OOP) in Python

## 🚀 Introduction

OOP helps:

* Improve **code reusability**
* Reduce **redundancy**
* Model **real-world scenarios**
* Build scalable systems

---

## 🧠 Programming Paradigms

### 1. Procedural Programming

Code is written step-by-step in sequence.

```python
a = 10
b = 20

sum = a + b
print(sum)

diff = a - b
print(diff)
```

---

### 2. Functional Programming

Introduces **functions** to:

* Reduce redundancy
* Improve reusability

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

---

### 3. Object-Oriented Programming (OOP)

Uses:

* **Classes**
* **Objects**

To model real-world entities.

---

## 🧩 Class and Object

### 🔹 Class

A **blueprint** for creating objects.

### 🔹 Object

An **instance** of a class.

---

### ✅ Example: Basic Class

```python
class Student:
    name = "Karan"
```

### Creating Objects

```python
s1 = Student()
print(s1.name)
```

**Output:**

```
Karan
```

---

## 🏗️ Constructor (`__init__`)

* Automatically called when an object is created
* Used to initialize object data

---

### ✅ Example: Constructor

```python
class Student:
    def __init__(self):
        print("Adding new student in database")

s1 = Student()
```

**Output:**

```
Adding new student in database
```

---

## 🔑 `self` Keyword

* Refers to the **current object**
* Used to access instance variables

---

### ✅ Example

```python
class Student:
    def __init__(self):
        print(self)

s1 = Student()
print(s1)
```

**Output:**

```
<__main__.Student object at 0x...>
<__main__.Student object at 0x...>
```

---

## 🧾 Parameterized Constructor

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Karan", 97)
s2 = Student("Arjun", 88)

print(s1.name, s1.marks)
print(s2.name, s2.marks)
```

**Output:**

```
Karan 97
Arjun 88
```

---

## 📊 Attributes

### 🔹 Instance Attributes

* Unique for each object

```python
self.name
self.marks
```

---

### 🔹 Class Attributes

* Shared across all objects

```python
class Student:
    college_name = "ABC College"
```

---

### ✅ Example

```python
class Student:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

s1 = Student("Karan")
print(s1.college_name)
print(Student.college_name)
```

**Output:**

```
ABC College
ABC College
```

---

### ⚠️ Priority Rule

If same name exists:

* Instance attribute > Class attribute

---

## ⚙️ Methods

Functions inside a class.

---

### ✅ Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Welcome", self.name)

s1 = Student("Karan")
s1.welcome()
```

**Output:**

```
Welcome Karan
```

---

### Another Example

```python
class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

s1 = Student(95)
print(s1.get_marks())
```

**Output:**

```
95
```

---

## 🧪 Practice: Student Average

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print(f"Hi {self.name}, your average score is {avg}")

s1 = Student("Tony Stark", [99, 98, 97])
s1.get_average()
```

**Output:**

```
Hi Tony Stark, your average score is 98.0
```

---

## 🔄 Static Methods

* Do **not use `self`**
* Work at **class level**

---

### ✅ Example

```python
class Student:
    @staticmethod
    def hello():
        print("Hello")

Student.hello()
```

**Output:**

```
Hello
```

---

## 🧱 Pillars of OOP

### 1. Abstraction

Hide internal details, show only essentials.

#### Example:

```python
class Car:
    def start(self):
        print("Car started")
```

User doesn’t know internal engine logic.

---

### 2. Encapsulation

Binding data + methods together.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

---

## 🏦 Practice: Bank Account System

```python
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} debited")
        print("Balance:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} credited")
        print("Balance:", self.balance)

    def get_balance(self):
        return self.balance
```

---

### ✅ Usage

```python
acc1 = Account(10000, 12345)

acc1.debit(1000)
acc1.credit(500)
```

**Output:**

```
1000 debited
Balance: 9000
500 credited
Balance: 9500
```

---

## 🎯 Key Takeaways

* Class = Blueprint
* Object = Instance
* `__init__` = Constructor
* `self` = Current object
* Attributes = Data
* Methods = Functions inside class
* Static Methods = No `self`
* OOP helps structure code better

---
