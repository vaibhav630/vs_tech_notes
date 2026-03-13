Perfect! Let's build a **fixture-style example** in plain JS using **a single function** that handles both success and error cases, similar to how Playwright fixtures work.

```js
// --- 1) Fake async data fetch (returns a Promise) ---
function fetchData(id, delay = 500) {
  return new Promise((resolve, reject) => {
    console.log(`[fetchData] started for id=${id}`);

    setTimeout(() => {
      if (typeof id !== 'number') {
        reject(new Error('Invalid id (must be a number)'));
        return;
      }

      resolve({ id, message: `Data for ${id}` });
    }, delay);
  });
}

// --- 2) Fixture-style function ---
async function dataFixture(id, runTest) {
  console.log("🔧 Setup: preparing data...");

  try {
    const value = await fetchData(id); // fetch data (may resolve or reject)
    await runTest(null, value);        // pass null error and value to test
  } catch (err) {
    await runTest(err, null);          // pass error to test
  }

  console.log("🧹 Teardown: cleaning up...");
}

// --- 3) Example test using the fixture ---
async function testHandler(err, data) {
  if (err) {
    console.error("❌ Test received error:", err.message);
  } else {
    console.log("✅ Test received data:", data);
  }
}

// --- 4) Run tests ---
(async () => {
  // success case
  await dataFixture(42, testHandler);

  // failure case
  await dataFixture('not-a-number', testHandler);
})();
```

### How this works, step by step:

1. **`fetchData(id)`** returns a Promise. It may resolve (success) or reject (error).
2. **`dataFixture(id, runTest)`** is the "fixture":

   * Setup happens first (`console.log("Setup…")`)
   * Calls `fetchData` with `await` to get the value or catch an error.
   * Calls `runTest` with `(err, data)` depending on the result.
   * Teardown happens last (`console.log("Teardown…")`)
3. **`testHandler(err, data)`** is your test code, which receives either a value or an error.
4. Both positive and negative scenarios are handled **inside the same fixture**.

---

If you want, I can also **rewrite this to accept multiple test inputs in an array** so a single fixture can run all positive and negative test cases sequentially — just like a mini test suite.

Do you want me to do that next?
