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

👉 Do you want me to also show you how to **switch an existing repo** (already cloned with HTTPS) to use SSH, instead of recloning?


Perfect 👍 you don’t need to reclone at all. You can simply **switch the remote URL from HTTPS → SSH**.

Here’s how you do it step by step:

---

## 🔹 1. Check current remotes

Inside your repo, run:

```bash
git remote -v
```

You’ll likely see something like:

```
origin  https://github.com/vaibhav630/vs_tech_notes.git (fetch)
origin  https://github.com/vaibhav630/vs_tech_notes.git (push)
```

---

## 🔹 2. Update the remote URL to SSH

Replace HTTPS with SSH:

```bash
git remote set-url origin git@github.com:vaibhav630/vs_tech_notes.git
```

---

## 🔹 3. Verify the change

Run:

```bash
git remote -v
```

Now it should show:

```
origin  git@github.com:vaibhav630/vs_tech_notes.git (fetch)
origin  git@github.com:vaibhav630/vs_tech_notes.git (push)
```

---

## 🔹 4. Test SSH connection

Before pushing/pulling, test:

```bash
ssh -T git@github.com
```

* If your key is set up correctly, you’ll see:

  ```
  Hi vaibhav630! You've successfully authenticated, but GitHub does not provide shell access.
  ```

---

✅ That’s it! Your repo is now switched to SSH, no reclone needed.

---

👉 Do you want me to also show you how to **do this for all future repos automatically** (so you never accidentally clone with HTTPS again)?

Nice 👍 If you always want to use **SSH instead of HTTPS** when cloning GitHub repos, you can set this up once and forget about it.

---

## 🔹 Option 1: Git global config (rewrite rule)

Tell Git to **rewrite HTTPS GitHub URLs into SSH automatically**:

```bash
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

Now whenever you do:

```bash
git clone https://github.com/vaibhav630/vs_tech_notes.git
```

Git will **silently convert it** into:

```bash
git clone git@github.com:vaibhav630/vs_tech_notes.git
```

---

## 🔹 Option 2: Always copy SSH clone URLs

On GitHub’s web UI:

* The green **“Code”** button → choose **SSH** tab instead of HTTPS.
* That way you always start with the right URL.

---

## 🔹 Option 3: SSH Config (advanced, if you have multiple accounts/keys)

In `~/.ssh/config`:

```ssh
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/github_vaibhav
```

This way SSH knows exactly which key to use when you connect to GitHub.

---

✅ Best practice: use **Option 1** if you want Git to handle it transparently, and **Option 3** if you ever deal with multiple GitHub accounts.

---

**if I go with option 1, how to revert it in future**


Great foresight 👌 If you use **Option 1** (`insteadOf` rule), you can remove or override it anytime.

---

### 🔹 To see your current setting:

```bash
git config --global --get-regexp url
```

You’ll see something like:

```
url.git@github.com:.insteadOf https://github.com/
```

---

### 🔹 To remove the rule:

```bash
git config --global --unset url."git@github.com:".insteadOf
```

---

### 🔹 To revert all at once (careful: wipes all URL rewrites you may have set):

```bash
git config --global --remove-section url."git@github.com:"
```

---

✅ After this, Git will stop rewriting HTTPS → SSH, and cloning via HTTPS will work as normal.

---

👉 Do you want me to also show you how to **set a per-project insteadOf rule** (only for one repo, not global)? That’s useful if you want work repos SSH-only but personal ones default.
