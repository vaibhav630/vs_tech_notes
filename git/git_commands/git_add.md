👍 You want to **stage everything except one file or folder**.

There are a couple of ways:

---

## 🔹 1. Use `git add` with pathspec negation

```bash
git add . ':!filename'
```

or for a folder:

```bash
git add . ':!foldername/'
```

👉 Explanation:

* `.` → add everything
* `':!filename'` → exclude that file

Example:

```bash
git add . ':!.env'
```

This stages all files except `.env`.

---

## 🔹 2. Multiple exclusions

```bash
git add . ':!secret.txt' ':!config.json'
```

---

## 🔹 3. With subdirectories

If the file is inside a folder:

```bash
git add . ':!src/debug.log'
```

---

⚠️ Notes:

* The quotes (`'`) are important in shells like zsh.
* This works in modern Git (≥ 1.8.4).

---

✅ If you do this often, better option is to add the file/dir to `.gitignore`, then `git add .` will always skip it.

---
