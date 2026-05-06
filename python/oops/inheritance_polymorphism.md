# Python OOP -- Inheritance and Polymorphism

This document explains **Object-Oriented Programming in Python (Part
3)** focusing on:

-   Inheritance
-   Base classes and derived classes
-   Method overriding
-   Adding new methods
-   Polymorphism
-   Abstract base class concept

------------------------------------------------------------------------

# 1. What is Inheritance?

Inheritance allows a **new class to reuse properties and methods of an existing class**.

Benefits:

-   Code reuse
-   Reduced complexity
-   Easier maintenance

Terminology:

- Base Class:      Original class
- Derived Class:   New class that inherits from base class

------------------------------------------------------------------------

# 2. Creating a Base Class

Example: Animal class

``` python
class Animal:

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")
```

Creating an instance

``` python
myanimal = Animal()
```

Output

    ANIMAL CREATED

------------------------------------------------------------------------

# 3. Creating a Derived Class

We can inherit from the base class.

Example: Dog inherits from Animal

``` python
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
```

Creating an instance

``` python
mydog = Dog()
```

Output

    ANIMAL CREATED
    Dog Created

------------------------------------------------------------------------

# 4. Using Inherited Methods

The derived class automatically gets methods from the base class.

``` python
mydog.eat()
mydog.who_am_i()
```

Output

    I am eating
    I am an animal

Even though these methods were defined in **Animal**, they are available in **Dog**.

------------------------------------------------------------------------

# 5. Overriding Methods

We can **override** base class methods.

Example:

``` python
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")
```

Now:

``` python
mydog = Dog()
mydog.who_am_i()
```

Output

    I am a dog

The Dog class **overrides** the original method.

------------------------------------------------------------------------

# 6. Adding New Methods

Derived classes can add their own methods.

Example:

``` python
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("WOOF!")
```

Usage

``` python
mydog = Dog()
mydog.bark()
```

Output

    WOOF!

------------------------------------------------------------------------

# 7. What is Polymorphism?

Polymorphism means **different classes can share the same method name
but behave differently**.

Example:

Dog and Cat both have `speak()` methods.

------------------------------------------------------------------------

# 8. Dog Class Example

``` python
class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"
```

------------------------------------------------------------------------

# 9. Cat Class Example

``` python
class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"
```

------------------------------------------------------------------------

# 10. Creating Instances

``` python
niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())
```

Output

    Niko says woof!
    Felix says meow!

Both classes share the **same method name `speak()`**.

------------------------------------------------------------------------

# 11. Polymorphism with a Loop

``` python
for pet in [niko, felix]:
    print(pet.speak())
```

Output

    Niko says woof!
    Felix says meow!

Even though objects are different types, the same method call works.

------------------------------------------------------------------------

# 12. Polymorphism with Functions

Example function

``` python
def pet_speak(pet):
    print(pet.speak())
```

Usage

``` python
pet_speak(niko)
pet_speak(felix)
```

Output

    Niko says woof!
    Felix says meow!

The function doesn't need to know whether the object is a Dog or Cat.

------------------------------------------------------------------------

# 13. Abstract Base Class Concept

Sometimes we create classes **only to be inherited**.

Example:

``` python
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
```

This class is **not meant to be instantiated directly**.

------------------------------------------------------------------------

# 14. Implementing Subclasses

Dog subclass

``` python
class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"
```

Cat subclass

``` python
class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"
```

------------------------------------------------------------------------

# 15. Example Usage

``` python
fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())
```

Output

    Fido says woof!
    Isis says meow!

------------------------------------------------------------------------

# 16. Real World Example of Polymorphism

Example: File handling

Different classes could share a method name:

    .open()

Examples:

- CSV file:     CSVReader
- Excel file:   ExcelReader
- PDF file:     PDFReader

Each class implements its own version of `.open()`.

------------------------------------------------------------------------

# 17. Summary

## Inheritance

Allows a class to reuse methods from another class.

Example

    class Dog(Animal)

------------------------------------------------------------------------

## Polymorphism

Different classes share the **same method name**.

Example:

    dog.speak()
    cat.speak()

------------------------------------------------------------------------

# 18. Key Concepts

-  Base Class:          Parent class
-  Derived Class:       Child class
-  Method Overriding:   Redefining a parent method
-  Polymorphism:        Same method name, different behavior
-  Abstract Class:      Class designed only for inheritance
