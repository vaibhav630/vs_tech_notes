You can **set Git configs** at different levels.

---

## 🔹 Levels of Git Configuration

1. **System level** → applies to all users on the system

   ```bash
   git config --system key value
   ```
2. **Global level** → applies to your user (recommended for name/email)

   ```bash
   git config --global key value
   ```
3. **Local level** → applies only to the repository you’re inside

   ```bash
   git config --local key value
   ```

---

## 🔹 Common Git Configurations

### 1. Set your name & email (global)

```bash
git config --global user.name "Vaibhav Sharma"
git config --global user.email "your_email@example.com"
```

### 2. Set default editor (example: VS Code)

```bash
git config --global core.editor "code --wait"
```

### 3. Set default branch name to `main`

```bash
git config --global init.defaultBranch main
```

### 4. Enable colored output

```bash
git config --global color.ui auto
```

### 5. Store credentials (cache or manager)

* Cache for a session:

  ```bash
  git config --global credential.helper cache
  ```
* Store permanently:

  ```bash
  git config --global credential.helper store
  ```
* Use system keychain (recommended on macOS/Windows):

  ```bash
  git config --global credential.helper manager
  ```

### 6. Check what’s set

```bash
git config --list
```

or for a specific one:

```bash
git config user.name
git config user.email
```

---
