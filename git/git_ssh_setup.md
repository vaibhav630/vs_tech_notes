You want to use **SSH for GitHub (or any Git server)** and configure Git properly on your system, here’s the step-by-step guide:

---

## 🔹 Step 1: Check for existing SSH keys

Run:

```bash
ls -al ~/.ssh
```

Look for files like:

* `id_rsa` & `id_rsa.pub` (RSA key pair)
* `id_ed25519` & `id_ed25519.pub` (modern, recommended)

If nothing exists → generate a new one.

---

## 🔹 Step 2: Generate a new SSH key (recommended: ED25519)

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

* `-C` is just a label (use your GitHub email).
* Press **Enter** to accept default file path.
* Enter a **passphrase** for extra security (or leave empty if you want no prompt).

This creates two files:

* `~/.ssh/id_ed25519` → private key (keep safe, never share)
* `~/.ssh/id_ed25519.pub` → public key (this goes to GitHub/GitLab)

---

## 🔹 Step 3: Add your SSH key to the agent

Start the ssh-agent:

```bash
eval "$(ssh-agent -s)"
```

Add your key:

```bash
ssh-add ~/.ssh/id_ed25519
```

---

## 🔹 Step 4: Add SSH key to GitHub

Copy the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the whole line that starts with `ssh-ed25519 ...`.

Go to GitHub:

* Settings → **SSH and GPG keys** → New SSH key
* Paste the key and save.

---

## 🔹 Step 5: Test the connection

```bash
ssh -T git@github.com
```

If successful, you’ll see:

```
Hi vaibhav630! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 🔹 Step 6: Configure Git (global)

Set your identity:

```bash
git config --global user.name "Vaibhav Sharma"
git config --global user.email "your_email@example.com"
```

Optional: set colors, default branch, etc.

```bash
git config --global color.ui auto
git config --global init.defaultBranch main
```

---

## 🔹 Step 7: Clone using SSH

Instead of HTTPS, always use SSH URLs:

```bash
git clone git@github.com:username/repo.git
```

---

✅ Now Git is configured with SSH → no need to enter username/password or PAT every time.
Your GitHub SSH key + agent handles authentication.

---