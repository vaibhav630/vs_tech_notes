Here’s the **clean and reliable way to install NVM using Homebrew** on your Mac 👇

---

## 🚀 Step 1: Install NVM via Homebrew

Run this in your terminal:

```bash
brew install nvm
```

---

## 📁 Step 2: Create NVM directory

NVM needs a dedicated folder:

```bash
mkdir ~/.nvm
```

---

## ⚙️ Step 3: Configure your shell (VERY IMPORTANT)

If you're using **zsh (default on Mac)**:

```bash
nano ~/.zshrc
```

Add this at the end:

```bash
export NVM_DIR="$HOME/.nvm"
source $(brew --prefix nvm)/nvm.sh
```

Save and exit:

* Press `CTRL + X`
* Then `Y`
* Then `Enter`

---

## 🔄 Step 4: Reload your terminal

```bash
source ~/.zshrc
```

---

## ✅ Step 5: Verify installation

```bash
nvm --version
```

If you see a version (like `0.39.x`), you're good 👍

---

## 📦 Step 6: Install Node.js using NVM

```bash
nvm install --lts
```

Set it as default:

```bash
nvm alias default node
```

---

## 🧠 Pro Tips

* Check available Node versions:

  ```bash
  nvm ls-remote
  ```

* Switch anytime:

  ```bash
  nvm use 18
  ```

---

If you want, I can also:

* Set up Node + npm + global packages properly
* Or help you fix common issues (like command not found, path issues, etc.)
