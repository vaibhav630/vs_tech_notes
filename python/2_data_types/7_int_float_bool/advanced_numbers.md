# Advanced Python Numbers -- Notes and Examples

This document summarizes **Advanced Number Operations in Python**
including:

-   Hexadecimal representation
-   Binary representation
-   Built‑in numeric functions (`pow`, `abs`, `round`)

------------------------------------------------------------------------

# 1. Hexadecimal Representation

Python can convert numbers to **hexadecimal (base‑16)** using `hex()`.

Example

``` python
print(hex(12))
```

Output

    0xc

Another example

``` python
print(hex(512))
```

Output

    0x200

Explanation

-   `0x` indicates hexadecimal format.

------------------------------------------------------------------------

# 2. Binary Representation

Binary numbers (base‑2) can be generated using `bin()`.

Example

``` python
print(bin(128))
```

Output

    0b10000000

Another example

``` python
print(bin(512))
```

Output

    0b1000000000

Explanation

-   `0b` indicates binary format.

------------------------------------------------------------------------

# 3. Power Function

We usually calculate powers using:

``` python
2 ** 4
```

Output

    16

Python also provides the **pow()** function.

``` python
print(pow(2,4))
```

Output

    16

------------------------------------------------------------------------

# 4. pow() with Modulus

`pow()` can take **three arguments**.

Syntax

    pow(x, y, z)

Equivalent to

    (x ** y) % z

Example

``` python
print(pow(2,4,3))
```

Output

    1

Explanation

    2^4 = 16
    16 % 3 = 1

This version is **more efficient for large numbers**.

------------------------------------------------------------------------

# 5. Absolute Value

The `abs()` function returns the **absolute value** of a number.

Example

``` python
print(abs(-5))
```

Output

    5

Example

``` python
print(abs(3))
```

Output

    3

------------------------------------------------------------------------

# 6. round() Function

The `round()` function rounds numbers.

Example

``` python
print(round(3.1))
```

Output

    3

Example

``` python
print(round(3.9))
```

Output

    4

------------------------------------------------------------------------

# 7. Rounding with Precision

You can specify **decimal precision**.

Example

``` python
print(round(3.1415926,2))
```

Output

    3.14

Explanation

-   Rounded to **2 decimal places**.

------------------------------------------------------------------------

# 8. Summary Table

  Function   Purpose
  ---------- -------------------------------
  hex()      Convert number to hexadecimal
  bin()      Convert number to binary
  pow()      Power calculation
  abs()      Absolute value
  round()    Rounding numbers

------------------------------------------------------------------------

# 9. Example -- Practical Usage

Binary conversion

``` python
num = 25
print(bin(num))
```

Output

    0b11001

Hex conversion

``` python
print(hex(num))
```

Output

    0x19

------------------------------------------------------------------------

# 10. Key Takeaways

Important built‑in number functions

    hex()
    bin()
    pow()
    abs()
    round()

Python also provides a powerful **math library**:

``` python
import math
```

which includes functions like:

    sqrt()
    sin()
    cos()
    log()
    factorial()

------------------------------------------------------------------------
