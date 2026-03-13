Let’s break down snippet 1 **step by step** and explain all the important keywords and how control flows.

---

### **Code**

```js
async function helloFixture() {
  // pretend we did some setup
  return "Hello World";
}

// use it
(async () => {
  const msg = await helloFixture();
  console.log(msg); // Hello World
})();
```

---

### **Step-by-Step Explanation**

| Line / Part                             | Explanation                                                                                                                                                                                                                                                                                               |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `async function helloFixture() { ... }` | Declares a **function** named `helloFixture` that is `async`. <br> - `async` keyword means this function **always returns a Promise**. <br> - You can use `await` inside it to wait for other Promises.                                                                                                   |
| `return "Hello World";`                 | Inside an `async` function, `return` automatically **resolves the Promise**. <br> This is equivalent to `return Promise.resolve("Hello World")`.                                                                                                                                                          |
| `(async () => { ... })();`              | This is an **Immediately Invoked Async Function Expression (IIAFE)**. <br> - `async () => { ... }` is an anonymous async arrow function. <br> - `()` at the end **calls it immediately**. <br> This is used to allow `await` at the top level, because `await` can only be used inside `async` functions. |
| `const msg = await helloFixture();`     | - `await` waits for the Promise returned by `helloFixture()` to **resolve**. <br> - The resolved value (`"Hello World"`) is stored in the variable `msg`. <br> Without `await`, `msg` would be a **Promise object** instead of the string.                                                                |
| `console.log(msg);`                     | Prints the resolved value `"Hello World"` to the console.                                                                                                                                                                                                                                                 |

---

### **Control Flow**

1. The async IIAFE starts executing immediately.
2. It calls `helloFixture()`.

   * `helloFixture()` returns a Promise that will resolve to `"Hello World"`.
3. The `await` pauses execution inside the IIAFE until the Promise resolves.
4. Once the Promise resolves, `"Hello World"` is assigned to `msg`.
5. `console.log(msg)` prints the value.
6. The IIAFE completes execution.

---

### **Key Takeaways**

* `async` → marks a function that returns a Promise.
* `await` → pauses execution until a Promise resolves.
* `return` in `async` → resolves the Promise.
* `(async () => { ... })();` → lets you use `await` at the top-level.

---

Let’s visualize the timeline of async code step by step.
**draw a timeline diagram showing exactly when the function starts, pauses at `await`, and resumes** — that makes async behavior really clear.

---

### **Timeline Diagram for Async/Await**

```text
Time -->
|------------------------------------------|

1. (IIAFE starts) 
(async () => {
   const msg = await helloFixture();  <--- Execution enters here
```

---

```text
2. helloFixture() is called
async function helloFixture() {
   return "Hello World"; 
}
```

* `helloFixture()` **returns a Promise** immediately.
* Execution **pauses at `await`** inside the IIAFE until the Promise resolves.

---

```text
3. Promise resolves
- The returned Promise from helloFixture() resolves with value "Hello World".
- Execution **resumes** at `await helloFixture()`.
```

---

```text
4. Value assignment
const msg = "Hello World";  <-- msg now holds the resolved value
```

---

```text
5. Logging
console.log(msg);  <-- Prints "Hello World" to the console
```

---

```text
6. End
- IIAFE completes execution
```

---

### **Flowchart Representation**

```
IIAFE starts
     |
     v
Call helloFixture() --> returns Promise
     |
     v
Pauses at await until Promise resolves
     |
     v
Promise resolves with "Hello World"
     |
     v
msg = "Hello World"
     |
     v
console.log(msg) --> "Hello World"
     |
     v
IIAFE ends
```

---

✅ **Key Points from Timeline**

1. `await` pauses only the async function (here, the IIAFE).
2. `helloFixture()` immediately returns a Promise.
3. Execution outside the async function is not blocked — only inside the IIAFE it waits.
4. `return "Hello World"` inside async automatically resolves the Promise.
