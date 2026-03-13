Here’s the **condensed Markdown notes** for your **Handling iFrames in Playwright** transcript:

---

# 📌 Handling iFrames in Playwright

## 🔹 What is an iFrame?

* **iFrame (inline frame)** → allows embedding one HTML document inside another.
* Used to **display external apps, sections, or modal frames** inside a page.
* In automation:

  * **If element is inside an iframe → must switch to the frame first.**
  * Otherwise, Playwright won’t find the element.

---

## 🔑 Identifying an iFrame

* Inspect element → check if inside `<frame>` or `<iframe>`.
* Frames usually have attributes:

  * `src`, `name`, `title`
* Tools like **SelectorsHub** will show you if element is inside a frame.

---

## ❌ Without Switching to iFrame

```js
await page.goto("url");

// Trying to click directly
await page.locator('//a[text()="java.applet"]').click();
```

👉 Fails → Playwright looks in the **main page DOM**, but element is in a **frame**.

* Test times out (30s default).

---

## ✅ Correct Way – Using Frame Locator

1. **Locate the frame**

```js
const iframe = page.frameLocator('iframe[name="packageListFrame"]');
```

2. **Interact with element inside the frame**

```js
await iframe.locator('//a[text()="java.applet"]').click();
```

3. (Optional) Pause to debug

```js
await page.pause();
```

---

## 🔄 Steps to Work with iFrames

1. Inspect → confirm element is in `<iframe>`.
2. Choose locator for frame (`src`, `name`, `title`, etc.).
3. Use `page.frameLocator("selector")` to **switch context**.
4. Use `.locator()` inside the frame to interact with elements.

---

## 🧑‍💻 Example: Redbus Login Modal

* Login popup is also an **iframe**.
* Steps are the same:

  * Switch to frame containing the modal.
  * Interact with input fields & buttons.

---

## ⚡ Key Takeaways

* **Frames and iFrames are the same** in Playwright context.
* Must **switch to frame** before interacting.
* Use `frameLocator` (recommended way).
* Once inside → can `click`, `type`, etc. normally.
* Works across all browsers with Playwright.

---

Do you want me to also make a **side-by-side cheatsheet** (❌ without frame vs ✅ with frame) like I did for Auto-suggestions, so you can keep it handy?
