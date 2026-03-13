## object destructuring in JavaScript**
---

### 1. What `require('@playwright/test')` returns

That module exports an object roughly like this (simplified):

```js
module.exports = {
  test: function test() { /* ... */ },
  expect: function expect() { /* ... */ },
  beforeEach: function beforeEach() { /* ... */ },
  afterEach: function afterEach() { /* ... */ },
  // ... more
};
```

---

### 2. How destructuring works

When you write:

```js
const { test, expect } = require('@playwright/test');
```

you’re not saving the whole module into two different variables — you’re doing **destructuring assignment**.

* `require('@playwright/test')` returns an object 
(the Playwright Test runner exports an object with multiple properties like `test`, `expect`, `beforeEach`, etc.).
* By writing `{ test, expect }`, you’re **picking out specific properties** from that object and creating local constants for them.

JavaScript looks at the property **names** in the curly braces:

* It finds a property named `test` on the object → assigns it to the local constant `test`.
* It finds a property named `expect` on the object → assigns it to the local constant `expect`.

So this line is basically syntactic sugar for:

```js
const tmp = require('@playwright/test');
const test = tmp.test;
const expect = tmp.expect;
```

---

### 3. Why `beforeEach` is not picked

Because you didn’t ask for it 😅.
Destructuring doesn’t randomly assign things. It’s a **pattern match by property name**.
If you want `beforeEach`, you’d have to explicitly destructure it:

```js
const { test, expect, beforeEach } = require('@playwright/test');
```

---

✅ In short:

* Destructuring is **name-based**.
* Only the keys you specify are pulled out.
* There’s no guessing or swapping — `test` will never get `beforeEach` unless you wrote it that way.

Nothing is duplicated, no extra memory overhead. You’re just extracting references to those properties from the same module export.
