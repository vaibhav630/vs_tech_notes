# JavaScript Loops – Quick Reference Guide

## What are Loops?

* A loop is a block of code that executes repeatedly until a condition is met.
* Useful when working with multiple elements (e.g., arrays, DOM nodes).

---

## 1. `for` Loop

### Syntax

```js
for (initialization; condition; increment/decrement) {
  // code to execute
}
```

### Example – Counting Up

```js
for (let x = 0; x < 10; x++) {
  console.log("Value is " + x);
}
// Output: 0 to 9
```

### Example – Counting Down

```js
for (let x = 10; x > 0; x--) {
  console.log(x);
}
// Output: 10 to 1
```

### Example – Custom Step

```js
for (let x = 0; x <= 20; x += 2) {
  console.log(x);
}
// Output: 0, 2, 4, …, 20
```

### Example – initialization before loop

```js
let x = 0
for (; x <= 20; x += 2) {
  console.log(x);
}
// Output: 0, 2, 4, …, 20
```

```js
let y = 0
for (; y <= 20;) {
  console.log(x);
  y +=2
}
// Output: 0, 2, 4, …, 20
```

---

## 2. `for` Loop with Arrays

```js
let arr = [12, 20, 56, "Hello", true];

for (let i = 0; i < arr.length; i++) {
  console.log("Array value:", arr[i]);
}
```

---

## 3. `forEach()` Method

```js
arr.forEach((element) => {
  console.log("Using forEach:", element);
});
```

---

## 4. `for...of` Loop

* Iterates over **values** in an iterable (arrays, strings, etc.).

```js
for (let value of arr) {
  console.log("Using for...of:", value);
}
```

```js
let name = "Selenium Webdriver";
for (let ch of name) {
  console.log(ch);
}
// Output: S, e, l, e, n, i, u, m, ...
```

---

## 5. `for...in` Loop

* Iterates over **keys/indexes**.
* Typically used for objects.

### With Arrays

#### returns index of array

```js
for (let index in arr) {
  console.log("index: ", index);
}
```

#### returns values of array

```js
for (let index in arr) {
  console.log(index, arr[index]);
}
```

### With Objects

```js
let myObj = { name: "Vaibhav", marks: 50, status: false };

for (let key in myObj) {
  console.log(key, ":", myObj[key]);
}
```

---

## 6. `while` Loop

### Syntax

```js
while (condition) {
  // code
}
```

### Example

```js
let sum = 5;
while (sum <= 15) {
  console.log("Sum is:", sum);
  sum++;
}
// Output: 5 to 15
```

---

## 7. `do...while` Loop

* Executes **at least once**, even if condition is false.

```js
let y = 10;
do {
  console.log("Value is:", y);
  y++;
} while (y < 15);
```

---

## 8. `break` and `continue`

### `break`

* Exits the loop immediately.

```js
for (let x = 0; x <= 10; x++) {
  if (x === 5) break;
  console.log(x);
}
// Output: 0–4
```

### `continue`

* Skips current iteration, moves to next.

```js
for (let x = 0; x <= 10; x++) {
  if (x === 4) continue;
  console.log(x);
}
// Output: 0,1,2,3,5,6,...10
```

---

✅ **Quick Tips**:

* Use **`for...of`** with arrays/strings.
* Use **`for...in`** with objects.
* Use **`while`** when condition-based repetition is needed.
* Use **`do...while`** when the block must run at least once.

---

Do you want me to also **split this into smaller `.md` guides** (like `for-loop.md`, `while-loop.md`, `foreach.md`) for easier lookup, or keep everything in **one single guide**?
