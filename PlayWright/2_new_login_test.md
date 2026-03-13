Here’s a clean, structured Markdown version of your lecture notes from the transcript:

````markdown
# Playwright: Interacting with Web Elements

## Introduction
- Focus of this lecture: How to interact with web elements in Playwright.
- Previous lectures covered:
  - Playwright installation
  - Writing the first script
- Recommended for beginners to watch the last three videos for setup and basics.

---

## Demo Application
- Using a **login form** (not full registration)
- Web elements covered:
  - Buttons
  - Input fields
  - Assertions for login/logout success
- Later topics will cover:
  - Radio buttons
  - Checkboxes
  - Dropdowns
  - Links

---

## Setting Up the Spec File
1. Create a new file: `login.spec.js`
2. Import Playwright Test functions:
   ```javascript
   const { test, expect } = require('@playwright/test');
````

* `test` → Write test cases
* `expect` → Assertions

---

## Test Credentials

* Username: `admin`
* Password: `admin123`
* Purpose:

  * Verify login is successful
  * Verify logout works properly
* Assertion options:

  * URL
  * Page content (dashboard, search, charts, etc.)

---

## Writing a Test

### 1. Define the test

```javascript
test('valid login', async ({ page }) => {
  await page.goto('https://example.com/login');
});
```

* `page` → Fixture to interact with web page
* `goto()` → Opens a specific URL

### 2. Interact with Input Fields

* **Username**

  ```javascript
  await page.getByPlaceholder('Username').type('admin');
  ```
* **Password**

  ```javascript
  await page.getByPlaceholder('Password').type('admin123');
  ```

### 3. Interact with Buttons

* Click the login button using XPath:

  ```javascript
  await page.locator('//button[@type="submit"]').click();
  ```

---

## Assertions

* URL verification after login:

```javascript
await expect(page).toHaveURL(/dashboard/);
```

* Use patterns for partial matching (e.g., `/dashboard/`)

---

## Running the Test

* Command:

```bash
npx playwright test ./tests/login.spec.js --headed
```

* `--headed` → Runs in visible browser mode (not headless)
* Common issues:

  * **Async/await**: Ensure function is `async` when using `await`.
  * **Timeouts**: Default is 30s; adjust if needed in config.

---

## Logout Test

1. Click profile icon:

```javascript
await page.getByAltText('profile picture').first().click();
```

2. Click logout:

```javascript
await page.getByText('Logout').click();
```

3. Verify URL after logout:

```javascript
await expect(page).toHaveURL(/login/);
```

4. Handle strict mode violation:

   * Playwright may find multiple elements with same text.
   * Use `.first()` or unique selectors.

---

## Optional Waits

* Debugging only (not recommended for production):

```javascript
await page.waitForTimeout(5000); // waits 5 seconds
```

---

## Typing Like a Human

* Slow down typing for realism using `delay`:

```javascript
await page.getByPlaceholder('Username').type('admin', { delay: 100 });
await page.getByPlaceholder('Password').type('admin123', { delay: 100 });
```

* `delay` → milliseconds per character (e.g., 100ms = 0.1s)

---

## Tools & Plugins

* **Selectors Hub** (Chrome extension)

  * Helps write XPath, CSS, jQuery selectors
  * Features:

    * Debugging
    * Code generation
    * Validation

---

## Reporting

* Generate Playwright test report:

```bash
npx playwright show-report
```

* Includes:

  * Before/After hooks
  * Commands executed
  * Passed/failed assertions
  * Duration

---

## Tips & Best Practices

* Use unique selectors for reliable tests.
* Avoid unnecessary `waitForTimeout`.
* Leverage new Playwright locator methods:

  * `getByPlaceholder`
  * `getByText`
  * `getByLabel`
  * `locator()`
* Use assertions (`expect`) to validate URLs, page elements, or text.
* Debugging failures helps learn correct selectors and workflows.

---

## Next Steps

* Practice with:

  * Dropdowns
  * Radio buttons
  * Checkboxes
* Explore advanced locator strategies and Playwright features.

```

---

If you want, I can also create a **visual flow diagram of the login/logout Playwright flow** to add to these notes—it makes it super easy to remember the steps.  

Do you want me to do that?
```
