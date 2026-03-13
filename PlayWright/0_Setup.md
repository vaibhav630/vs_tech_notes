# Playwright Installation & Setup Guide

## Prerequisites
- **Node.js** (v14 or above recommended, LTS preferred).
  - Check version: `node -v`
- **Visual Studio Code** for writing tests.

## Installation
1. Create a project folder (e.g., `learn_playwright`).
2. Open the folder in VS Code.
3. Open terminal inside the folder.
4. Run:
   ```bash
   npm init playwright@latest
    ```

* Choose **JavaScript** or **TypeScript**.
* Default test folder: `tests/`
* Optionally skip GitHub Actions.
* Install Playwright browsers when prompted.

## Project Structure

* **package.json** → Dependencies & scripts.
* **playwright.config.js** → Core configurations:

  * Test directory
  * Timeout
  * Parallel execution
  * Browsers (Chromium, Firefox, WebKit by default)
  * Reporters
* **tests/** → Sample test files.
* **node\_modules/** → Dependencies.

## Running Tests

* Run all tests:

  ```bash
  npx playwright test
  ```

  * Runs in **headless mode** by default.
  * Executes in **3 browsers** in parallel.

* Run in headed mode:

  ```bash
  npx playwright test --headed
  ```

* View report:

  ```bash
  npx playwright show-report
  ```

## Reporters Available

* HTML (default)
* Line, List, Dot
* JSON, JUnit
* GitHub Actions, Annotations
* Third-party reporters

## Key Takeaways

* One command sets up Playwright: `npm init playwright@latest`.
* By default:

  * Tests run **parallel in 3 browsers**.
  * Reports are **auto-generated**.
* Use `--headed` to view browser actions.

---

# Playwright Setup Cheatsheet

## Setup
```bash
npm init playwright@latest
````

## Check Node.js

```bash
node -v
```

## Run Tests

```bash
npx playwright test        # Run all tests (headless, 3 browsers)
npx playwright test --headed   # Run in headed mode
```

## Reports

```bash
npx playwright show-report
```

## Config File

* `playwright.config.js` → settings (browsers, reporters, timeouts, parallel).


