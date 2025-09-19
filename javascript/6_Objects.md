# JavaScript Objects – Complete Guide

This guide covers everything about **objects in JavaScript**, including how to create, access, add, delete, and nest them.

---

## 🔹 What is an Object?

- An **object** in JavaScript is a collection of **named values** (key–value pairs).
- Keys are called **properties**, and values can be of **any type** (string, number, boolean, object, array, function, etc).
- In other languages:
  - **Java** → similar to `Map`
  - **Python** → similar to `Dictionary`

---

## 🔹 Creating Objects

### Empty Object
```js
let obj1 = {};
console.log(typeof obj1); // "object"
````

### Object with Properties

```js
let obj2 = {
  name: "Vaibhav",
  address: "Bangalore",
  number: 1234567890,
  status: false
};
console.log(obj2);
```

---

## 🔹 Accessing Properties

* **Dot notation**:

```js
console.log(obj2.name);    // "Vaibhav"
console.log(obj2.number);  // 1234567890
```

* **Bracket notation**:

```js
console.log(obj2["name"]);     // "Vaibhav"
console.log(obj2["address"]);  // "Bangalore"
```

* **Non-existing property**:

```js
console.log(obj2.salary);  // undefined
```

---

## 🔹 Adding Properties

```js
obj2.salary = 100;
obj2.experience = 1;
console.log(obj2);
```

---

## 🔹 Deleting Properties

```js
delete obj2.salary;
console.log(obj2);
```

---

## 🔹 Nested Objects

```js
let obj3 = {
  state: "Karnataka",
  country: "India"
};

obj2.fullAddress = obj3;
console.log(obj2);
```

Access nested values:

```js
console.log(obj2.fullAddress.country); // "India"
```

---

## 🔹 Arrays Inside Objects

```js
obj2.myFamily = ["m1", "m2"];
console.log(obj2.myFamily[1]); // "m2"
```

---

## 🔹 Functions Inside Objects

```js
obj2.myFunction = function() {
  console.log("Hello from function");
};

obj2.myFunction(); // Hello from function
```

---

## 🔹 Objects are Reference Types

```js
let Vaibhav = obj2;
delete Vaibhav.fullAddress;

console.log(obj2.fullAddress); // undefined (deleted from both)
```

Adding via one reference affects the other:

```js
obj2.randomValue = "test";
console.log(Vaibhav.randomValue); // "test"
```

⚠️ Objects are **not copied by value**, but by **reference**.

---

## 🔹 Summary

* Objects = collection of properties (key–value pairs).
* Create with `{}` or object literals.
* Access with dot `.` or bracket `["key"]`.
* Add properties dynamically.
* Delete properties with `delete`.
* Can contain other objects, arrays, and functions.
* Objects are assigned **by reference**, not value.