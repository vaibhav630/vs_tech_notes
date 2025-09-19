# JavaScript Conditionals – Quick Reference

---

## 1. `if` Statement
Executes a block only if the condition is `true`.

```javascript
if (true) {
  console.log("I am inside if block"); // ✅ prints
}

if (false) {
  console.log("This will not run");
}
```

### Example with numbers:
```javascript
if (10 < 20) {
  console.log("10 is less than 20");
}
```

---

## 2. `if...else`
Provides an alternative block when the condition is `false`.

```javascript
if (10 > 20) {
  console.log("I am inside if block");
} else {
  console.log("I am inside else block"); // ✅ executes
}
```

---

## 3. `if...else if...else`
Used when checking **multiple conditions**.

```javascript
let browserName = "chrome";

if (browserName.includes("chrome")) {
  console.log("Chrome started");
} else if (browserName.includes("firefox")) {
  console.log("Firefox started");
} else if (browserName.includes("edge")) {
  console.log("Edge started");
} else {
  console.log("This tool only supports Firefox, Chrome, and Edge browsers");
}
```

### Supports multiple branches:
```javascript
let browserName = "ff"; 

if (browserName.includes("firefox") || browserName.includes("ff")) {
  console.log("Firefox started (alias ff supported)");
}
```

---

## 4. `switch` Statement
Simplifies multiple equality checks.

```javascript
let day = 0;

switch (day) {
  case 0:
    console.log("Sunday");
    break;
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  default:
    console.log("Sorry, not a valid day");
}
```

### With real date:
```javascript
let date = new Date();
let today = date.getDay(); // 0=Sunday, 1=Monday, ... 6=Saturday

switch (today) {
  case 0: console.log("Sunday"); break;
  case 1: console.log("Monday"); break;
  case 2: console.log("Tuesday"); break;
  case 3: console.log("Wednesday"); break;
  case 4: console.log("Thursday"); break;
  case 5: console.log("Friday"); break;
  case 6: console.log("Saturday"); break;
  default: console.log("Invalid day");
}
```

---

## 5. Notes
- `if` checks a **boolean expression**.
- `else` is optional but provides fallback behavior.
- `else if` lets you chain multiple conditions.
- `switch` is great for exact value matches (use `break` to avoid fall-through).
- `default` in `switch` is like `else` – optional, but recommended.

---

✅ Use conditionals in testing, automation, and app logic to **control code execution** based on runtime conditions.
