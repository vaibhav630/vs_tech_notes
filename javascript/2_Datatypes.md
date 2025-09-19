# JavaScript Data Types

---

Data is the most important part of any programming language. In JavaScript, data types are divided into two main categories:

- **Primitive**
- **Non-Primitive (Reference)**

---

## 1. Primitive Data Types
Primitive data types are basic and immutable. JavaScript provides:

- `string`
- `number`
- `boolean`
- `null`
- `undefined`
- `bigint`
- `symbol`

### Note
In this course, focus is on `string`, `number`, `boolean`, `null`, and `undefined`.  
`bigint` and `symbol` are excluded.

### Wrapper Objects
Except `null` and `undefined`, all primitive data types have wrapper objects (e.g., `String`, `Number`, `Boolean`).

---

## 2. Examples of Primitive Types

### String
```javascript
let fname = "Vaibhav";
console.log(fname);           // Vaibhav
console.log(typeof fname);    // string
```

### Number

```javascript
let marks = 98.5;
console.log(typeof marks);    // number
console.log(marks);           // 98.5
```

* In JavaScript, all numeric values (integer, float, negative) are of type `number`.

### Boolean

```javascript
let status = true;
console.log(typeof status);   // boolean
console.log(status);          // true
```

### Undefined

```javascript
let lname;
console.log(lname);           // undefined
console.log(typeof lname);    // undefined
```

### Null

```javascript
let address = null;
console.log(address);         // null
console.log(typeof address);  // object (known JavaScript bug)
```

---

## 3. Dynamic Typing

JavaScript is a **dynamically typed language** — variables can hold different data types over time:

```javascript
let x = 10;
console.log(typeof x);    // number

x = true;
console.log(typeof x);    // boolean

x = "Vaibhav";
console.log(typeof x);    // string

x = undefined;
console.log(typeof x);    // undefined

x = null;
console.log(typeof x);    // object
```

---

## 4. Non-Primitive Data Types

Non-primitive data types are objects or references.

### Objects

```javascript
let person = {
  firstName: "Vaibhav",
  lastName: "Sharma"
};

console.log(typeof person);  // object
console.log(person);         // { firstName: "Vaibhav", lastName: "Sharma" }
```

### Arrays

```javascript
let studentMarks = [10, 20, 30];
console.log(typeof studentMarks);  // object
console.log(studentMarks);         // [10, 20, 30]
```

> In JavaScript, **everything that is not primitive is an object**.

---

## 5. Key Notes

* JavaScript primitives: `string`, `number`, `boolean`, `null`, `undefined`, `bigint`, `symbol`.
* Except for `null` and `undefined`, primitives have wrapper objects.
* `typeof null` returns `object` (historical bug).
* Non-primitives like `objects` and `arrays` are reference types and return `object` with `typeof`.

---

### Diagram/Cheatsheet table

```
| Category          | Data Type   | Example Code                       | `typeof` Result  |
| ----------------- | ----------- | ---------------------------------- | ---------------- |
| **Primitive**     | `string`    | `let name = "Vaibhav";`             | `"string"`       |
|                   | `number`    | `let marks = 98.5;`                | `"number"`       |
|                   | `boolean`   | `let status = true;`               | `"boolean"`      |
|                   | `undefined` | `let x;`                           | `"undefined"`    |
|                   | `null`      | `let y = null;`                    | `"object"` (bug) |
| **Non-Primitive** | `object`    | `let person = { name: "Vaibhav" };` | `"object"`       |
|                   | `array`     | `let arr = [1,2,3];`               | `"object"`       |
    
```
