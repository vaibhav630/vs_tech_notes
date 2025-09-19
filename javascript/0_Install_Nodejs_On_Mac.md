# Install Node.js (LTS) on macOS (Package Installer)

Follow these steps to install the latest **LTS version** of Node.js on macOS using the official package installer.

---

## 1. Download LTS Installer
Go to the official Node.js website:

👉 [https://nodejs.org/en/download](https://nodejs.org/en/download)

- Select **macOS Installer (.pkg)** under **LTS**.

---

## 2. Run the Installer
1. Open the downloaded `.pkg` file.
2. Follow the on-screen instructions.
3. The installer will set up both **Node.js** and **npm**.

---

## 3. Set PATH Variable (if prompted)

Open Terminal & Edit `~/.zshrc`:

```bash
vi ~/.zshrc
```
If .zshrc is not available in home directory, then create new file:

```bash
touch .zshrc
```

Add lines:

```bash
export PATH=/usr/local/bin:$PATH
```

If Node.js was installed elsewhere, find its location with:

```bash
which node
```
and replace /usr/local/bin with the correct path.
Save and exit (:wq).

Save & reload:

```bash
source ~/.zshrc
```

Verify Installation:

```bash
node -v
npm -v
```

Both should print version numbers.