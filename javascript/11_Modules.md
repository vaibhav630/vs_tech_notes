# JavaScript Modules Quick Reference

## What is a Module?
- A **module** is a reusable unit of code (a file).
- Helps in:
  - **Reusability** – use the same code across files.
  - **Maintainability** – modify only the affected module.
  - **Separation of concerns** – divide large applications into smaller parts.

---

## 1. User-Defined Modules

### students.js
```js
function showStudentName() {
  console.log("Student name is Vaibhav");
}

function showCollegeName() {
  console.log("College name is NIIST");
}

// Export functions
module.exports = { showCollegeName, showStudentName };
````

### moduleDemo.js

```js
const students = require("./students");

students.showCollegeName(); // ✅ College name is NIIST
students.showStudentName(); // ✅ Student name is Vaibhav
```

---

## 2. Inbuilt Modules

### Using `os`

```js
const os = require("os");

console.log(os.platform());   // e.g., win32
console.log(os.type());       // e.g., Windows_NT
console.log(os.hostname());   // e.g., LAPTOP-1234
```

### Using `assert`

```js
const assert = require("assert");

// Passing assertion
assert(50 < 60, "Value mismatched"); // ✅ no error

// Failing assertion
assert(50 > 60, "Value mismatched"); // ❌ AssertionError
```

---

## Recap

* **`module.exports`** is used to share code.
* **`require()`** imports user-defined or inbuilt modules.
* Common inbuilt modules: `os`, `assert`, `fs`, `zlib`, etc.