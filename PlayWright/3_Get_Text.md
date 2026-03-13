Here’s a clean Markdown version of your transcript notes:

````markdown
# Playwright: Capturing and Verifying Error Messages

## Introduction
- Topic: How to capture and verify error messages in Playwright.
- Importance:
  - Verification is critical in testing.
  - Ensures that tests provide meaningful validation.
- Example used: **Orange HRM login**
  - Concept applies to any application and type of message (tooltip, alerts, etc.).

---

## Scenario
1. Valid credentials → successful login → continue test.
2. Invalid credentials → display **"Invalid credentials"** message → verify it.

---

## Setting Up the Test
1. Spec file: `verify_errormessage.spec.js`
2. Import Playwright test functions:
```javascript
const { test, expect } = require('@playwright/test');
````

3. Create the test:

```javascript
test('verify error message', async ({ page }) => {
  await page.goto('https://example.com/login');
});
```

---

## Interacting with Login Fields

* **Username**

```javascript
await page.getByPlaceholder('Username').type('admin');
```

* **Password** (using invalid credentials)

```javascript
await page.getByPlaceholder('Password').type('wrongpassword');
```

* **Login Button** (XPath example)

```javascript
await page.locator('//button[@type="submit"]').click();
```

---

## Capturing Error Message

1. Inspect the error message element (`<p>` tag, class: `alert-content-text`).
2. Use XPath or CSS to locate it:

```javascript
const errorMessageLocator = await page.locator("//p[contains(@class, 'alert-content-text')]");
```

3. Capture text:

```javascript
const errorMessage = await errorMessageLocator.textContent();
console.log('Error message is:', errorMessage);
```

* Methods:

  * `textContent()` → Single element text
  * `allTextContents()` → Array of multiple element texts

---

## Assertions

### Partial Match

```javascript
expect(errorMessage.includes('invalid')).toBeTruthy();
```

* Checks if the error message contains a specific keyword.

### Exact Match

```javascript
expect(errorMessage).toBe('Invalid credentials');
```

* Checks the full string.
* Missing characters will cause the test to fail.

---

## Running the Test

* Run specific spec file:

```bash
npx playwright test tests/verify_errormessage.spec.js --headed
```

* `--headed` → Run in visible browser mode.
* Observations:

  * Console.log shows captured messages.
  * Partial vs full match assertions behave differently.

---

## Handling Failures

* If message does not match:

  * Test fails
  * Playwright report shows received vs expected values
* Reports can auto-open on failure or be configured manually:

```bash
npx playwright show-report
```

---

## Tips & Best Practices

* Multiple ways exist to capture messages; this is one approach.
* Always verify messages as part of test validation.
* Use `getByPlaceholder`, `locator()`, or XPath/CSS selectors depending on element attributes.
* Partial match is useful for dynamic content.
* Exact match is useful for strict validation.

---

## Optional: Slowing Typing

* To emulate human typing:

```javascript
await page.getByPlaceholder('Username').type('admin', { delay: 100 });
```

* `delay` in milliseconds per character.

---

## Summary

* Error message verification is essential in automated testing.
* Capturing message:

  * Locate element
  * Extract text using `textContent()` or `allTextContents()`
* Assertions:

  * Partial or full string validation
* Reports show results clearly, including failures for debugging.

```

---
