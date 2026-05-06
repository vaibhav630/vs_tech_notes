# Python Decorators -- Step‑by‑Step Guide

This document summarizes the concept of **Python decorators** and the
concepts required to understand them.

------------------------------------------------------------------------

# 1. Functions are Objects in Python

Functions can be assigned to variables.

``` python
def hello():
    return "Hello!"

greet = hello
print(greet())
```

Output:

    Hello!

Even if we delete the original function name:

``` python
del hello
print(greet())
```

Output:

    Hello!

Explanation:

`greet` still points to the original function object.

------------------------------------------------------------------------

# 2. Nested Functions

Functions can be defined inside other functions.

``` python
def hello():
    print("The hello() function has been executed")

    def greet():
        return "\tThis is the greet function inside hello"

    def welcome():
        return "\tThis is welcome inside hello"

    print(greet())
    print(welcome())
    print("End of hello function")

hello()
```

Output:

    The hello() function has been executed
        This is the greet function inside hello
        This is welcome inside hello
    End of hello function

Important:

`greet()` and `welcome()` only exist **inside** `hello()`.

------------------------------------------------------------------------

# 3. Returning Functions from Functions

A function can return another function.

``` python
def hello(name="Jose"):

    print("The hello() function has been executed")

    def greet():
        return "\tThis is the greet function inside hello"

    def welcome():
        return "\tThis is welcome inside hello"

    print("I am going to return a function")

    if name == "Jose":
        return greet
    else:
        return welcome


my_new_func = hello()
print(my_new_func())
```

Output:

    The hello() function has been executed
    I am going to return a function
        This is the greet function inside hello

Explanation:

`hello()` returned the function `greet`.

------------------------------------------------------------------------

# 4. Another Simple Example

``` python
def cool():

    def super_cool():
        return "I am very cool!"

    return super_cool


some_func = cool()
print(some_func())
```

Output:

    I am very cool!

------------------------------------------------------------------------

# 5. Passing Functions as Arguments

Functions can also be passed as parameters.

``` python
def hello():
    print("Hi Jose!")


def other(func):
    print("Other code runs here!")
    func()


other(hello)
```

Output:

    Other code runs here!
    Hi Jose!

Explanation:

`hello` is passed into `other` and executed inside it.

------------------------------------------------------------------------

# 6. Building a Decorator Manually

Now we combine everything.

``` python
def new_decorator(original_function):

    def wrap_func():

        print("Some extra code before the original function")

        original_function()

        print("Some extra code after the original function")

    return wrap_func
```

------------------------------------------------------------------------

# 7. Function That Needs Decoration

``` python
def func_needs_decorator():
    print("I want to be decorated!")
```

Manually decorating:

``` python
decorated_function = new_decorator(func_needs_decorator)
decorated_function()
```

Output:

    Some extra code before the original function
    I want to be decorated!
    Some extra code after the original function

------------------------------------------------------------------------

# 8. Using the @ Decorator Syntax

Python provides a simpler syntax.

``` python
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()
```

Output:

    Some extra code before the original function
    I want to be decorated!
    Some extra code after the original function

This is equivalent to:

    func_needs_decorator = new_decorator(func_needs_decorator)

------------------------------------------------------------------------

# 9. Why Decorators Are Useful

Decorators allow you to add functionality such as:

-   Logging
-   Authentication
-   Timing execution
-   Input validation
-   Web routing (Flask / Django)

Example:

``` python
@timer
def my_function():
    pass
```

The decorator automatically adds extra behavior without modifying the
function.

------------------------------------------------------------------------

# 10. Key Takeaways

Decorators rely on three core Python concepts:

1.  **Functions are objects**
2.  **Functions can be returned from other functions**
3.  **Functions can be passed as arguments**

A decorator simply:

    wraps a function with extra functionality

using:

    @decorator_name

------------------------------------------------------------------------
