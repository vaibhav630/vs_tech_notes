
# JavaScript Variables, Scope & Constants

**Topic:** Difference between `var`, `let`, and `const` in JavaScript

---

## 🔹 1. Introduction
When learning JavaScript, one common source of confusion is the difference between `var`, `let`, and `const`.  
Understanding these properly helps in avoiding bugs related to **scope**, **redeclaration**, and **immutability**.

---

## 🔹 2. `var`
- Can be **declared** and **updated**.
- Can also be **redeclared**.
- Scope: **Function-scoped** (not block-scoped).

```js
var name = "Vaibhav";
var name = "Sharma"; // redeclaration allowed
console.log(name); // Sharma
````

⚠️ Variables declared with `var` are accessible **outside blocks**, which can lead to unintended behavior.

---

## 🔹 3. `let`

* Can be **declared** and **updated**.
* ❌ Cannot be **redeclared** in the same scope.
* Scope: **Block-scoped** (exists only inside `{ }`).

```js
let city = "Bangalore";
city = "Pune"; // ✅ update allowed
// let city = "Delhi"; ❌ redeclaration not allowed
console.log(city); // Pune
```

---

## 🔹 4. `const`

* Must be initialized at the time of declaration.
* ❌ Cannot be updated.
* ❌ Cannot be redeclared.
* Scope: **Block-scoped**.

```js
const country = "India";
// country = "USA"; ❌ error
console.log(country); // India
```

---

## 🔹 5. Summary Table

| Feature       | `var`           | `let`         | `const`       |
| ------------- | --------------- | ------------- | ------------- |
| Redeclaration | ✅ Allowed       | ❌ Not allowed | ❌ Not allowed |
| Update value  | ✅ Allowed       | ✅ Allowed     | ❌ Not allowed |
| Scope         | Function-scoped | Block-scoped  | Block-scoped  |

---

## 🔹 6. Loops with `let` vs `var`

```js
for (var i = 0; i < 3; i++) {
  console.log(i); // 0, 1, 2
}
console.log(i); // 3 (still accessible ❌)

for (let j = 0; j < 3; j++) {
  console.log(j); // 0, 1, 2
}
console.log(j); // ReferenceError (not accessible ✅)
```

---

## 🔹 7. Undefined & Errors

* If you try to **access a variable before declaration** with `let`/`const`, you’ll get a **ReferenceError** (Temporal Dead Zone).
* With `var`, you may get **`undefined`**, which can be misleading.

---

## 🔹 8. Key Takeaways

* Use **`let`** for variables that will change.
* Use **`const`** for variables that should never change.
* Avoid `var` in modern JavaScript — it creates unexpected behaviors due to function scoping.

---

✅ By understanding `var`, `let`, and `const`, you write safer, more predictable JavaScript code.

