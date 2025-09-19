# JavaScript Strings

Strings in JavaScript can be created as **primitive values** or as **objects**.

---

## 1. Creating Strings
```javascript
// Primitive string
let fname = "Vaibhav";
console.log(typeof fname);   // string

// String object
let lname = new String("Sharma");
console.log(typeof lname);   // object
````

* **Primitive string** → immutable, lightweight.
* **String object** → created with `new String()`, behaves like an object.

---

## 2. String Properties & Indexing

```javascript
let str = "My name is Vaibhav Sharma";

console.log(str.length);  // 24
console.log(str[0]);      // 'M'
console.log(str[1]);      // 'y'
```

---

## 3. Common String Methods

### Searching

```javascript
str.includes("Vaibhav");     // true
str.includes("Vaibhav");     // false (case-sensitive)

str.startsWith("My");       // true
str.endsWith("Sharma");     // true
```

### Splitting

```javascript
let arr = str.split(" ");
console.log(arr);           // ["My", "name", "is", "Vaibhav", "Sharma"]
console.log(arr[3]);        // "Vaibhav"
```

### Case Conversion

```javascript
str.toUpperCase();          // "MY NAME IS Vaibhav Sharma"
str.toLowerCase();          // "my name is Vaibhav Sharma"
```

### Trimming

```javascript
"   hello   ".trim();       // "hello"
```

### Replace

```javascript
str.replace("Sharma", "Modwani"); 
// "My name is Vaibhav Modwani"
```

---

## 4. Strings Are Immutable

Methods **do not change the original string**.

```javascript
let s = "hello";
let upper = s.toUpperCase();
console.log(s);     // "hello"
console.log(upper); // "HELLO"
```

---

## 5. Extracting Numbers from Strings

Example: `"The total price is 200 USD"`

```javascript
let msg = "The total price is 200 USD";
let parts = msg.split(" ");    // ["The","total","price","is","200","USD"]

let value = parts[4];          // "200" (string)
let price = parseInt(value);   // 200 (number)

if (price === 200) console.log("PASS");
else console.log("FAIL");
```

---

## 6. Template Literals (ES6+)

Use **backticks** (`` ` ``) for cleaner, multi-line, and dynamic strings.

```javascript
let x = 90;

// Multi-line string
let msg = `Final amount is
${x} USD in single quotes: 'quoted'`;

console.log(msg);
/*
Final amount is
90 USD in single quotes: 'quoted'
*/
```

---

## ✅ Recap

* Strings can be **primitive** or **object**.
* Key methods: `.length`, `[]` indexing, `.includes()`, `.startsWith()`, `.endsWith()`, `.split()`, `.toUpperCase()`, `.toLowerCase()`, `.trim()`, `.replace()`.
* Strings are **immutable**.
* Extract numbers using `.split()` + `parseInt()`.
* Use **template literals** for dynamic and cleaner strings.

---

# JavaScript String Methods – Cheat Sheet (with ES2023+)

| Method               | Purpose                              | Example                                    | Output                                |
|----------------------|--------------------------------------|--------------------------------------------|---------------------------------------|
| `.length`            | Get string length                   | `"hello".length`                           | `5`                                   |
| `[index]`            | Access character at position        | `"hello"[1]`                               | `"e"`                                 |
| `.at()` ⭐ (ES2022)   | Access char with negative index     | `"hello".at(-1)`                           | `"o"`                                 |
| `.includes()`        | Check substring (case-sensitive)    | `"hello".includes("ell")`                  | `true`                                |
| `.startsWith()`      | Check prefix                       | `"hello".startsWith("he")`                 | `true`                                |
| `.endsWith()`        | Check suffix                       | `"hello".endsWith("lo")`                   | `true`                                |
| `.split()`           | Split into array                   | `"a b c".split(" ")`                       | `["a","b","c"]`                       |
| `.toUpperCase()`     | Convert to uppercase               | `"hello".toUpperCase()`                    | `"HELLO"`                             |
| `.toLowerCase()`     | Convert to lowercase               | `"HELLO".toLowerCase()`                    | `"hello"`                             |
| `.trim()`            | Remove leading/trailing spaces     | `"  hi  ".trim()`                          | `"hi"`                                |
| `.trimStart()`       | Remove leading spaces              | `"  hi".trimStart()`                       | `"hi"`                                |
| `.trimEnd()`         | Remove trailing spaces             | `"hi  ".trimEnd()`                         | `"hi"`                                |
| `.replace()`         | Replace substring (first match)    | `"hello".replace("l","x")`                 | `"hexlo"`                             |
| `.replaceAll()` ⭐    | Replace all occurrences            | `"hello".replaceAll("l","x")`              | `"hexxo"`                             |
| `.match()`           | Match regex (returns array/null)   | `"abc123".match(/\d+/)`                    | `["123"]`                             |
| `.matchAll()` ⭐      | Match all regex results (iterator) | `[... "abc123abc456".matchAll(/\d+/g)]`    | `[["123"],["456"]]`                   |
| `.padStart()`        | Pad at start to given length       | `"5".padStart(3,"0")`                      | `"005"`                               |
| `.padEnd()`          | Pad at end to given length         | `"5".padEnd(3,"0")`                        | `"500"`                               |
| `.repeat()`          | Repeat string multiple times       | `"ha".repeat(3)`                           | `"hahaha"`                            |
| `.charAt()`          | Get char at index                  | `"hello".charAt(1)`                        | `"e"`                                 |
| `.charCodeAt()`      | Get UTF-16 code of char            | `"A".charCodeAt(0)`                        | `65`                                  |
| `String.fromCharCode()` | Convert UTF-16 code → char       | `String.fromCharCode(65)`                  | `"A"`                                 |
| `parseInt()`         | Convert string → integer           | `parseInt("200")`                          | `200`                                 |
| `parseFloat()`       | Convert string → float             | `parseFloat("3.14")`                       | `3.14`                                |
| Template Literals    | Multi-line / embed expressions     | `` `Total: ${5+5}` ``                      | `"Total: 10"`                         |


