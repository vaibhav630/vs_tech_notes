# Advanced Python Strings -- Notes and Examples

This document summarizes **Advanced String Methods in Python**
including:

-   Case conversion
-   Searching and counting
-   Formatting
-   Boolean string checks
-   Splitting and partitioning strings

------------------------------------------------------------------------

# 1. Creating a String

``` python
s = "hello world"
print(s)
```

Output

    hello world

------------------------------------------------------------------------

# 2. Changing Case

## capitalize()

Capitalizes the **first letter** of the string.

``` python
s = "hello world"
print(s.capitalize())
```

Output

    Hello world

------------------------------------------------------------------------

## upper()

Converts all letters to uppercase.

``` python
print(s.upper())
```

Output

    HELLO WORLD

------------------------------------------------------------------------

## lower()

Converts all letters to lowercase.

``` python
print(s.lower())
```

Output

    hello world

------------------------------------------------------------------------

# 3. Counting and Finding

## count()

Counts occurrences of a character.

``` python
s = "hello world"
print(s.count("o"))
```

Output

    2

------------------------------------------------------------------------

## find()

Returns index of **first occurrence**.

``` python
print(s.find("o"))
```

Output

    4

------------------------------------------------------------------------

# 4. Formatting Methods

## center()

Centers a string within a given width.

``` python
s = "hello"
print(s.center(20,"Z"))
```

Output

    ZZZZZZZhelloZZZZZZZZ

Explanation

Total length = 20 with padding `"Z"`.

------------------------------------------------------------------------

## expandtabs()

Expands tab characters.

``` python
s = "hello\thi"
print(s.expandtabs())
```

Output

    hello    hi

Useful when processing **text data containing tabs**.

------------------------------------------------------------------------

# 5. Boolean String Checks

These methods return **True or False**.

------------------------------------------------------------------------

## isalnum()

Checks if all characters are **alphanumeric**.

``` python
s = "hello123"
print(s.isalnum())
```

Output

    True

------------------------------------------------------------------------

## isalpha()

Checks if all characters are **alphabetic**.

``` python
s = "hello"
print(s.isalpha())
```

Output

    True

------------------------------------------------------------------------

## islower()

Returns True if all letters are **lowercase**.

``` python
s = "hello"
print(s.islower())
```

Output

    True

------------------------------------------------------------------------

## isspace()

Checks if the string contains **only whitespace**.

``` python
s = "   "
print(s.isspace())
```

Output

    True

------------------------------------------------------------------------

## istitle()

Checks if string is **title case**.

``` python
s = "Hello World"
print(s.istitle())
```

Output

    True

------------------------------------------------------------------------

## isupper()

Checks if all letters are **uppercase**.

``` python
s = "HELLO"
print(s.isupper())
```

Output

    True

------------------------------------------------------------------------

## endswith()

Checks if string ends with a specific substring.

``` python
s = "hello"
print(s.endswith("o"))
```

Output

    True

Equivalent to

``` python
s[-1] == "o"
```

------------------------------------------------------------------------

# 6. Split Method

Splits a string into a list using a separator.

``` python
s = "hello"
print(s.split("e"))
```

Output

    ['h', 'llo']

Example with multiple occurrences

``` python
s = "hi hi hi"
print(s.split("i"))
```

Output

    ['h', ' h', ' h', '']

Split occurs at **every occurrence**.

------------------------------------------------------------------------

# 7. Partition Method

Similar to split but returns **three parts**:

    (head, separator, tail)

Example

``` python
s = "hello"
print(s.partition("e"))
```

Output

    ('h', 'e', 'llo')

Explanation

  Part        Meaning
  ----------- -----------------------
  head        text before separator
  separator   the separator itself
  tail        text after separator

------------------------------------------------------------------------

# 8. Difference Between split() and partition()

  Method        Behavior
  ------------- ---------------------------------
  split()       Splits at every occurrence
  partition()   Splits at first occurrence only
  partition()   Returns separator as well

------------------------------------------------------------------------

# 9. Summary of Useful String Methods

  Method         Purpose
  -------------- -------------------------
  capitalize()   Capitalize first letter
  upper()        Convert to uppercase
  lower()        Convert to lowercase
  count()        Count occurrences
  find()         Find index of character
  center()       Center string
  expandtabs()   Replace tab characters
  isalnum()      Check alphanumeric
  isalpha()      Check alphabetic
  islower()      Check lowercase
  isupper()      Check uppercase
  istitle()      Check title case
  isspace()      Check whitespace
  endswith()     Check ending substring
  split()        Split string
  partition()    Split into 3 parts

------------------------------------------------------------------------

# 10. Key Takeaways

Most commonly used methods in real code:

    upper()
    lower()
    split()
    find()
    count()
    endswith()

Less common but useful:

    center()
    expandtabs()
    partition()

Boolean checks help with:

-   **text validation**
-   **natural language processing**
-   **data cleaning**
