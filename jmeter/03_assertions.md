# JMeter Beginner Tutorial – Assertions

---

Assertions in JMeter are **checks on server responses**.
They help validate correctness, performance, and format of the response.

---

## 1. Adding Assertions

* Right-click **Thread Group** → **Add → Assertions**
* Common assertions: Response, Duration, Size, XML/HTML, XPath

---

## 2. Commonly Used Assertions

### ✅ Response Assertion

* Validates **response code**, **text**, or **pattern**.
* Example: Check if response code = `200`.
* If mismatch → test fails.

---

### ⏱ Duration Assertion

* Validates response **time**.
* Set max duration (in ms).
* If response takes longer → test fails.

---

### 📦 Size Assertion

* Validates **response size (bytes)**.
* Conditions: `=`, `<`, `>`, `<=`, `>=`.
* Example: Fail if size < 30,000 bytes.

---

### 🌐 HTML / XML Assertions

* **HTML Assertion**: Validates response as valid HTML.

  * Can log errors/warnings to a file for detailed analysis.
* **XML Assertion**: Validates response as valid XML.

---

### 🔍 XPath Assertion

* Checks specific **nodes/values** in XML/HTML responses.
* Common in **API testing**.

---

## 3. Listener for Assertions

* Add **Assertion Results Listener** for debugging.
* Shows pass/fail for each assertion.
* ⚠️ Heavy on memory → disable for large load tests.

---

## 4. Best Practices

* Use assertions to ensure **correctness** under load.
* Keep checks realistic (not overly strict).
* Disable heavy listeners in load scenarios.

