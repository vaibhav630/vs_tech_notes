👉 How to **switch an existing repo** (already cloned with HTTPS) to use SSH, instead of recloning?

simply **switch the remote URL from HTTPS → SSH**.

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

👉 How to **do this for all future repos automatically** (so you never accidentally clone with HTTPS again)?

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

👌 If you use **Option 1** (`insteadOf` rule), you can remove or override it anytime.

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

👉 how to **set a per-project insteadOf rule** (only for one repo, not global)? That’s useful if you want work repos SSH-only but personal ones default.
