# Playwright — Writing Your First Script

## Before Starting
- Clean up default files if you want:
  - Delete pre-defined example tests.
  - Keep only:
    - `tests/` folder (empty)
    - `package.json`
    - `playwright.config.js`

---

## Creating First Test File
1. Create a new file inside `tests/`  
   Example: `sample.spec.js`

2. Import required Playwright test modules:
   ```js
   const { test, expect } = require('@playwright/test');
   ```

---

## Writing Tests

* **test()** → declares a test.
* **expect()** → writes assertions.

### Example

```js
test('my first test', async ({ page }) => {
  // test logic here
});
```

* Each test gets an isolated **page** fixture (browser page instance).
* Use `async/await` since Playwright functions return promises.

---

## Multiple Tests

```js
test('my first test', async ({ page }) => {});
test('my second test', async ({ page }) => {});
test('my third test', async ({ page }) => {});
```

* Running with `npx playwright test` executes all tests.
* Tests run across **3 browsers (Chromium, Firefox, WebKit)** → total tests = `#tests × 3`.

---

## Using Assertions

```js
expect(12).toBe(12);          // Pass
expect(100).toBe(101);        // Fail
expect(2.0).toBe(2.0);        // Pass
expect('Mukesh').toContain('Muk'); // Pass
expect(true).toBeTruthy();    // Pass
expect(false).toBeFalsy();    // Pass
```

---

## Controlling Tests

* Run **only one test**:

  ```js
  test.only('my fourth test', async ({ page }) => {});
  ```
* Skip a test:

  ```js
  test.skip('my second test', async ({ page }) => {});
  ```

---

## Reports

* Run tests:

  ```bash
  npx playwright test
  ```
* View HTML report:

  ```bash
  npx playwright show-report
  ```
* Report shows:

  * Passed/Failed/Skipped tests
  * Console output
  * Steps, hooks, retries

---

## Example: Verify Google Title

File: `google.spec.js`

```js
const { test, expect } = require('@playwright/test');

test('verify application title', async ({ page }) => {
  await page.goto('http://google.com');

  // Print title
  const title = await page.title();
  console.log('Title is:', title);

  // Assert
  await expect(page).toHaveTitle('Google');
});
```

* Must use **protocol** (`http://` or `https://`), otherwise navigation fails.
* Must use **await**, otherwise Playwright methods won’t work.

---

## Config Defaults

* Located in `playwright.config.js`
* Key setting:

  ```js
  expect: { timeout: 5000 } // 5 seconds default
  ```
* Controls how long Playwright waits for assertions.

---

## Recap

* Created `sample.spec.js` from scratch.
* Learned:

  * `test()` and `expect()`
  * `test.only` and `test.skip`
  * Basic assertions (`toBe`, `toContain`, `toBeTruthy`, `toBeFalsy`)
* Created `google.spec.js`:

  * Used `page.goto()`
  * Captured and asserted page title
* Learned importance of:

  * Protocol in URLs
  * `async/await`
  * Reports (`npx playwright show-report`)

---

✅ Next: Interacting with web elements and advanced assertions.

```

Do you want me to also create a **compact cheatsheet version** (like last time) just for this “first script” video?
```
