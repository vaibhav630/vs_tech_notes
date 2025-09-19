# JavaScript Operators – Quick Guide

In JavaScript, operators help manipulate data. They behave differently depending on the data types involved. This guide covers **arithmetic, assignment, comparison, logical, and type operators** (excluding bitwise for now).

---

## 1. Arithmetic Operators
```js
console.log(10 / 2);     // 5
console.log(10 / 2.5);   // 4
console.log(10 / 0);     // Infinity
console.log("abc" / 0);  // NaN
console.log(10 / null);  // Infinity
console.log(10 / undefined); // NaN
````

* Numbers divided by **0** → `Infinity`.
* Strings divided by **0** → `NaN`.
* `null` is treated as `0`.
* `undefined` → `NaN`.

**Type coercion example:**

```js
console.log("5" + 5);  // "55"  (string concatenation)
console.log("5" - 5);  // 0     (string converted to number)
```

---

## 2. Boolean in Arithmetic

```js
console.log(10 / true);   // 10  (true → 1)
console.log(10 / false);  // Infinity (false → 0)
console.log("5" * 5);     // 25
console.log("abc" * 5);   // NaN
```

---

## 3. Comparison Operators

* **Assignment (`=`)** – assign value.
* **Equality (`==`)** – compares values with type coercion.
* **Strict Equality (`===`)** – compares values without type coercion.

```js
let num1 = "50";  // string
let num2 = 50;    // number

console.log(num1 == num2);   // true  (type coercion)
console.log(num1 === num2);  // false (no coercion)
```

---

## 4. Logical Operators

```js
console.log(16 > 10);          // true
console.log(16 < 10);          // false
console.log(16 >= 16);         // true

console.log(10 > 8 && 10 > 5); // true
console.log(10 > 8 || 10 < 5); // true
console.log(!(true));          // false
```

---

## 5. String Comparisons

```js
let str1 = "This is JS";
let str2 = "JS";

// Check substring
console.log(str1.includes(str2));  // true

// Exact match (case-sensitive)
let str3 = "This is JS";
console.log(str1 === str3);  // true

// Case-insensitive comparison
console.log(str1.toUpperCase() === str3.toUpperCase()); // true
```

---

## 6. Assignment Operators

Shorthand forms:

```js
let num = 10;

num += 5;  // 15
num *= 5;  // 75
num /= 5;  // 15
```

Equivalent to writing `num = num + 5`, `num = num * 5`, etc.

---

## Key Takeaways

* **`==` vs `===`:** use `===` to avoid unexpected type coercion.
* Arithmetic operators behave differently with different types.
* Strings + numbers → concatenation, except with `-`, `*`, `/` (coercion to numbers).
* Logical operators behave as expected (`&&`, `||`, `!`).
* For string comparisons, use `includes()` for partial match, or normalize case for insensitive comparison.
* Use assignment operators (`+=`, `-=`, `*=`) for concise expressions.

---

👉 Explore [JavaScript MDN Docs on Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators) for deeper insights.


## JavaScript Operators Cheatsheet

## Arithmetic
```js
10 + 5    // 15
10 - 5    // 5
10 * 5    // 50
10 / 2    // 5
10 / 0    // Infinity
"5" + 5   // "55"  (concatenation)
"5" - 5   // 0     (coercion)
````

---

## Comparison

```js
5 == "5"   // true   (value only, coercion)
5 === "5"  // false  (value + type)
5 != "5"   // false
5 !== "5"  // true
10 > 5     // true
10 >= 10   // true
10 < 5     // false
```

---

## Logical

```js
true && false  // false
true || false  // true
!true          // false
```

---

## Boolean in Arithmetic

```js
10 / true   // 10   (true → 1)
10 / false  // Infinity (false → 0)
```

---

## String Checks

```js
"Hello JS".includes("JS");         // true
"JS".toUpperCase() === "js".toUpperCase(); // true (case-insensitive)
```

---

## Assignment (Shorthand)

```js
let x = 10;
x += 5;   // 15
x -= 5;   // 10
x *= 2;   // 20
x /= 2;   // 10
```

---

👉 Always prefer **`===`** over `==` to avoid unexpected type coercion.

