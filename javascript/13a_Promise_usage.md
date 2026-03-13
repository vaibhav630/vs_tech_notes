Below you get a **runnable example** that defines a function which **returns a Promise**, then consumes it using `await` (with `try/catch`) — plus the equivalent `.then/.catch` version and a step-by-step breakdown.

---

# Custom Promise + `await` — runnable example

```js
// promise-example.js

// --- 1) A function that returns a Promise ---
// It simulates an async operation (like fetching data).
function fetchData(id, delay = 500) {
  return new Promise((resolve, reject) => {
    // "executor" runs immediately and should call resolve/reject later
    console.log(`[fetchData] started for id=${id}`);

    // simulate async work with setTimeout
    setTimeout(() => {
      if (typeof id !== 'number') {
        // reject the promise on bad input
        reject(new Error('Invalid id (must be a number)'));
        return;
      }

      // simulate success payload
      const payload = { id, message: `Data for ${id}` };
      resolve(payload); // fulfill the promise
    }, delay);
  });
}

// --- 2) Consume with async/await + try/catch ---
async function runWithAwait() {
  console.log('\n--- runWithAwait START ---');
  try {
    // await pauses runWithAwait until the Promise resolves or rejects
    const data = await fetchData(42, 800);
    console.log('[runWithAwait] resolved:', data);
  } catch (err) {
    console.error('[runWithAwait] caught error:', err.message);
  }
  console.log('--- runWithAwait END ---\n');
}

// --- 3) Consume with .then/.catch (equivalent) ---
function runWithThen() {
  console.log('--- runWithThen START ---');
  fetchData(7, 300)
    .then((data) => {
      console.log('[runWithThen] resolved:', data);
    })
    .catch((err) => {
      console.error('[runWithThen] caught error:', err.message);
    })
    .finally(() => {
      console.log('--- runWithThen END ---\n');
    });
}

// --- 4) Demonstrate rejection handling with await ---
async function runErrorCase() {
  console.log('--- runErrorCase START ---');
  try {
    // intentionally passing a bad id to trigger reject
    const data = await fetchData('not-a-number', 400);
    console.log('[runErrorCase] resolved:', data);
  } catch (err) {
    console.error('[runErrorCase] caught error:', err.message);
  }
  console.log('--- runErrorCase END ---\n');
}

// Execute examples in sequence
(async () => {
  await runWithAwait();  // waits ~800ms inside
  runWithThen();         // starts, doesn't block main IIFE
  await runErrorCase();  // waits ~400ms and handles rejection
})();
```

### Expected console output (approximate order)

```
[fetchData] started for id=42
--- runWithAwait START ---
[runWithAwait] resolved: { id: 42, message: 'Data for 42' }
--- runWithAwait END ---

[fetchData] started for id=7
--- runWithThen START ---
[runWithThen] resolved: { id: 7, message: 'Data for 7' }
--- runWithThen END ---

[fetchData] started for id=not-a-number
--- runErrorCase START ---
[runErrorCase] caught error: Invalid id (must be a number)
--- runErrorCase END ---
```

---

## Step-by-step explanation (keywords & flow)

1. **`new Promise((resolve, reject) => { ... })`**

   * Creates a Promise object in **pending** state.
   * The executor function receives two functions:

     * `resolve(value)` → mark the promise **fulfilled** with `value`.
     * `reject(error)` → mark the promise **rejected** with `error`.
   * Executor runs synchronously right away, but typically you call `resolve/reject` asynchronously (e.g., in a callback or `setTimeout`).

2. **Inside `fetchData`**

   * We log a start message, then call `setTimeout` to simulate async work.
   * After `delay` ms we either call `resolve(payload)` (success) or `reject(new Error(...))` (failure).

3. **Consuming with `await`**

   * `await fetchData(42)` pauses the **async function** (`runWithAwait`) until the Promise settles.
   * If the Promise **resolves**, `await` returns the resolved value.
   * If the Promise **rejects**, `await` throws — so you catch it with `try/catch`.

4. **Consuming with `.then/.catch`**

   * `fetchData(...).then(onResolved).catch(onRejected)` registers callbacks.
   * This is functionally equivalent to `await` + `try/catch` but uses chaining instead of syntactic sugar.

5. **Order & concurrency**

   * `await` inside an `async` function suspends that function, but **does not block the whole Node thread**.
   * You can run multiple Promises concurrently by not `await`ing them immediately (e.g., kick them off first, then `await Promise.all([...])`).

---

## Small notes / best practices

* Prefer `async/await` for readability when you have sequential async logic.
* Use `.then/.catch` or `Promise.all()` for parallel workflows.
* Always handle rejections (either `.catch` or `try/catch`) — unhandled rejections become runtime errors.
* Inside an `async` function, `return x` is equivalent to `return Promise.resolve(x)`.

---

Want me to modify this to show **parallel execution** with `Promise.all` or to convert `fetchData` into something that actually fetches a URL?
