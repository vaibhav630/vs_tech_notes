---

⚡ Key difference:

* **Async version** → uses `await`, works well with promises and non-blocking operations.
* **Sync version** → runs everything immediately and blocks until done.

Do you want me to also show you a **hybrid fixture** that can work both ways (sync & async), like testing frameworks internally do?

---

# “How do I make my own fixture-like thing in plain JavaScript?”

In JavaScript, a **fixture** usually just means some *fixed test data* or *helper setup code* you can reuse. Let me show you a super-simple version that just returns `"Hello World"`.

---

## 1. Simplest Fixture (just a function)

```js
function helloFixture() {
  return "Hello World";
}

// use it
console.log(helloFixture()); // Hello World
```

---

## 2. Async Fixture (returns a Promise)

Sometimes fixtures mimic setup/teardown work, so you can make it async:

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

## 3. Fixture with Setup + Teardown

If you want it to behave more like test framework fixtures:

```js
async function helloFixture(runTest) {
  console.log("Setup: creating Hello World");
  const value = "Hello World";

  await runTest(value);

  console.log("Teardown: cleaning up Hello World");
}

// use it
helloFixture(async (hello) => {
  console.log("Test using:", hello); // Hello World
});
```

Output:

```
Setup: creating Hello World
Test using: Hello World
Teardown: cleaning up Hello World
```

---

## 4. Sync Fixture with Setup + Teardown


```js
// A sync fixture function
function helloFixture(runTest) {
  console.log("🔧 Setup: creating Hello World fixture...");
  const value = "Hello World";

  // Run the test code synchronously
  runTest(value);

  console.log("🧹 Teardown: cleaning up Hello World fixture...");
}

// Example usage of the fixture
helloFixture((hello) => {
  console.log("✅ Test started");
  console.log("Fixture gave me:", hello); // should print "Hello World"

  // simulate some work (blocking for demo)
  for (let i = 0; i < 1e8; i++) {} // busy loop

  console.log("✅ Test finished");
});
```

Output:

```
🔧 Setup: creating Hello World fixture...
✅ Test started
Fixture gave me: Hello World
✅ Test finished
🧹 Teardown: cleaning up Hello World fixture...
```

---

✅ So in **plain JS**, a fixture is just a function (sync or async) that provides some *fixed resource* (like `"Hello World"`, mock data, or a DB connection).

---

