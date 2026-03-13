Yes! You **can handle both success and error cases using the same function**. Right now, `runWithAwait` and `runErrorCase` are separate just for clarity, but you can pass a parameter to determine whether the test should succeed or fail. Here's how you can do it:

```js
// --- 1) A function that returns a Promise (same as before) ---
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

// --- 2) A single async function to handle both positive & negative cases ---
async function runTest(id, delay = 500) {
  console.log(`\n--- runTest START (id=${id}) ---`);
  try {
    const data = await fetchData(id, delay);
    console.log('[runTest] resolved:', data);
  } catch (err) {
    console.error('[runTest] caught error:', err.message);
  }
  console.log(`--- runTest END (id=${id}) ---\n`);
}

// --- 3) Execute both success and failure using the same function ---
(async () => {
  await runTest(42, 800);          // success
  await runTest('not-a-number', 400); // error
})();
```

### ✅ Key points:

1. `runTest` takes the `id` as input.
2. It **awaits** `fetchData`, so it pauses until the Promise resolves or rejects.
3. `try/catch` handles both success (resolve) and failure (reject) in one place.
4. No need for separate functions for positive and negative cases.

---

If you want, I can also rewrite this in a **fixture-style pattern** like Playwright, where you do `setup → test → teardown` using this single `runTest` for both success and failure. This makes it feel even more like test automation.

Do you want me to do that?
