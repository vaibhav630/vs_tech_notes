# JavaScript Functions – Complete Guide

---

## 🔹 What is a Function?

- A **function** is a set of statements that performs a particular task.
- You can **call** a function any number of times → main use is **reusability**.
- Functions can:
  - Take **parameters** (inputs)
  - Return **values** (outputs)
- In JavaScript:
  - Functions are also **objects** → more precisely, **function objects**.

---

## 🔹 Creating a Function

```js
function sayHello() {
  console.log("Hello JavaScript");
}
````

* To call:

```js
sayHello(); // Hello JavaScript
```

* If you don’t use parentheses (`sayHello`), nothing happens.
* Functions without a return statement → return `undefined`.

---

## 🔹 Function with Parameters & Return

```js
function showName(fname, lname) {
  return fname + " " + lname;
}

console.log(showName("Vaibhav", "Sharma")); // Vaibhav Sharma
```

* Without `return` → undefined.
* With `return` → value can be stored or printed.

---

## 🔹 Functions Are Objects

```js
console.log(typeof showName); // "function"
```

* Functions are **function objects** in JavaScript.

---

## 🔹 Function Expressions

Functions can be assigned to variables.

```js
function f1() {
  console.log("I am in f1");
  return 30;
}

let myFunc = f1;
myFunc(); // "I am in f1"
console.log(myFunc()); // "I am in f1", 30
console.log(typeof myFunc); // "function"
```

---

## 🔹 Anonymous Function Expressions

```js
let myFuncNew = function(num1, num2, num3) {
  return num1 + num2 + num3;
};

console.log(myFuncNew(12, 24, 36)); // 72
```

* Functions without names can still be stored in variables.

---

## 🔹 Functions Inside Objects

```js
let myObj = {
  name: "Vaibhav",
  f3: function() {
    console.log("I am inside object");
  }
};

myObj.f3(); // "I am inside object"
```

---

## 🔹 Functions Inside Arrays

```js
let arr = [
  12,
  "Vaibhav",
  function() {
    console.log("I am inside array");
  }
];

arr[2](); // "I am inside array"

// or store it
let y = arr[2];
y(); // "I am inside array"
```

---

## 🔹 Arrow Functions

Shorter syntax for function expressions.

### Normal Function

```js
let z = function() {
  console.log("Hello JS again");
};
z();
```

### Arrow Function

```js
let z = () => {
  console.log("Hello JS again");
};
z();
```

### With Parameters

```js
let add = (x1, x2) => {
  return x1 + x2;
};

console.log(add(12, 45)); // 57
```

---

## 🔹 One-Line Arrow Functions

If body has a single statement, you can omit `{}` and `return`.

```js
let myAddress = () => "Bangalore";
console.log(myAddress()); // Bangalore
```

---

## 🔹 Arrow Functions with Parameters + Template Literals

```js
let myAddressNew = (house, street) => `${house} ${street} Bangalore`;

console.log(myAddressNew("Sahaj", "Whitefield")); 
// "Sahaj Whitefield Bangalore"
```

---

## 🔹 Recap

1. Functions = set of reusable statements.
2. Defined using:

   * `function` keyword
   * Function expressions
   * Anonymous functions
   * Arrow functions
3. Functions can:

   * Accept parameters
   * Return values
   * Be stored in variables
   * Be stored inside objects/arrays
4. Functions are **function objects**.
5. Arrow functions:

   * Short syntax
   * Support parameters
   * Can be one-liners for simple tasks

---

✅ Functions are one of the most powerful and flexible features of JavaScript.
