Here’s a structured Markdown version of your transcript notes:

````markdown
# Playwright: Maximizing Screen & Changing Viewport

## Introduction
- Topic: How to maximize the screen or change viewport size in Playwright.
- Unlike Selenium:
  - Selenium has `driver.manage().window().maximize()`.
  - Playwright **does not have a direct maximize method**.
- Why important:
  - Prevents scrollbars or hidden elements.
  - Ensures consistent testing in full-screen-like mode.
  - Helps avoid test failures due to element visibility.

---

## Understanding Viewport
- Playwright uses **viewport** instead of direct maximize.
- Viewport defines **width** and **height** of the browser page.
- Scrollbars appear if viewport is smaller than page content.

### Checking Current Viewport
```javascript
console.log('Width:', page.viewportSize().width);
console.log('Height:', page.viewportSize().height);
````

* Example output:

  * Width: 1280
  * Height: 720

* Optional website to check screen size: [What is my viewport](https://www.whatismyviewport.com)

  * Example monitor resolution: 1920 × 1080

  * mine is 1470 × 804 in brave

---

## Setting Viewport

### 1. Global Configuration (All Tests)

* Modify `playwright.config.js`:

```javascript
use: {
  viewport: { width: 1920, height: 1080 }
}
```

* Applies to **all spec files** in the project.
* Ensures consistent viewport across tests.

### 2. Specific Test or Spec File

* Override viewport for a single test:

```javascript
test.use({ viewport: { width: 1500, height: 1000 } });
```

* Can be applied **per test or per spec file**.
* Useful for testing responsive designs or different screen sizes.

---

## Capturing Viewport Values

* You can **print width and height** to verify:

```javascript
console.log('Current width:', page.viewportSize().width);
console.log('Current height:', page.viewportSize().height);
```

* Helps ensure viewport is set correctly.

---

## Notes & Tips

* Viewport changes can prevent scroll-related issues.
* Adjust viewport based on:

  * Application layout
  * Monitor size
  * Testing requirements
* Global settings via `playwright.config.js` save repetitive configuration.
* Test-specific settings override global config if needed.

---

## Summary

* Playwright does not have a direct "maximize" method.
* Use **viewport size** to emulate full-screen or custom resolutions.
* Two ways to set viewport:

  1. **Global (config)** → applies to all tests
  2. **Test-specific** → overrides for a single test/spec file
* Verifying viewport ensures tests behave as expected in different screen sizes.

```

---
