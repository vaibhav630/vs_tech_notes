````markdown
# Lecture Notes: Arrays in JavaScript

**Speaker:** Vaibhav Sharma  
**Source:** Learn Hivernation

---

## Introduction
- Arrays are an **ordered list of values** in JavaScript.
- Unlike some other languages (Java, C#, Python), JavaScript arrays can hold **different types of values**:
  - Numbers
  - Strings
  - Booleans
  - Other arrays
  - Objects
  - Functions
- Arrays in JavaScript are **objects** (not primitive types).

---

## Creating Arrays
```js
let arr = [];             // Empty array
let arr2 = [10, 20, 30];  // Array with numbers
````

* Run with: `node arraydemo.js`
* `typeof arr` → `"object"`

---

## Accessing Values

* Index starts from `0`.

```js
let arr = [10, 20, 30];
console.log(arr[1]); // 20
console.log(arr[2]); // 30
console.log(arr[5]); // undefined (no error like Java's IndexOutOfBounds)
```

* Mixed values:

```js
let arr = [10, "Vaibhav", null, undefined, true];
console.log(arr[4]);        // true
console.log(typeof arr[4]); // boolean
```

---

## Array Properties

* **Length**: `arr.length`
* **Accessing last/second last elements**:

```js
console.log(arr[arr.length - 1]); // last element
console.log(arr[arr.length - 2]); // second last
```

---

## Common Methods

### Adding

* **push()** → add at end
* **unshift()** → add at start

```js
arr.push(100);     // Adds at end
arr.unshift("O2"); // Adds at start
```

### Removing

* **pop()** → remove from end (returns removed value)
* **shift()** → remove from start (returns removed value)

```js
arr.pop();   // Removes last element
arr.shift(); // Removes first element
```

### Splice

* **splice(start, count)** → remove specific elements

```js
arr.splice(1, 2); // Removes 2 elements starting at index 1
```

---

## Nested Arrays

* Arrays can hold other arrays:

```js
let arr1 = [10, "Vaibhav", true];
let arr2 = ["Java", "JavaScript", "Python"];

arr1.push(arr2);

console.log(arr1[3]);    // ["Java", "JavaScript", "Python"]
console.log(arr1[3][1]); // "JavaScript"
```

---

## Objects in Arrays

```js
let obj1 = { name: "Vaibhav Sharma", language: "JavaScript" };
arr1.push(obj1);

console.log(arr1[4].name); // "Vaibhav Sharma"
```

* Access with **dot notation** or **bracket notation**.

---

## Loops with Arrays

### Basic for loop

```js
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

### Iterating over complex arrays

Works the same even if array contains:

* Numbers
* Strings
* Booleans
* Nested arrays
* Objects

---

## Key Recap

1. Arrays can hold **any type of values**.
2. `typeof array` → `"object"`.
3. Index starts at **0**.
4. `length` gives the count.
5. **push / unshift** → add values.
   **pop / shift** → remove values.
   **splice** → remove specific values.
6. Arrays can contain **arrays**, **objects**, and even **functions**.
7. Loops (for, forEach, while) can be used to access array elements.

---

## Closing Notes

* Arrays in JavaScript are flexible and powerful.
* Next step: arrays containing **functions** (covered after learning functions).
* Practice with push, pop, unshift, shift, splice, and nested arrays.

**End of Lecture.**

```

Do you also want me to generate a **`.js` file** that matches these notes (like we did for operators), so you can directly run the examples step by step?
```
