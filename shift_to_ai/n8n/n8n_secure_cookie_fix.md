This error in **n8n** is quite common when running it locally on Mac. It’s basically saying:

> “I’m trying to use secure cookies (HTTPS), but you’re accessing me via HTTP.”

---

## 🔍 Why this happens

* n8n assumes **secure cookies = HTTPS**
* But you’re probably opening:

  * `http://<your-ip>:5678` ❌ (not secure)
* Or using a browser like **Safari**, which enforces stricter cookie rules

---

## ✅ Fix Options (Pick one)

### 🥇 Option 1: Use `localhost` (Quick fix)

Instead of using IP, open:

```
http://localhost:5678
```

✔ Works instantly
✔ No config needed
✔ Recommended for local dev

---

### 🥈 Option 2: Disable secure cookie (for local only)

Run n8n with this env variable:

```bash
export N8N_SECURE_COOKIE=false
n8n start
```

Or one-liner:

```bash
N8N_SECURE_COOKIE=false n8n
```

✔ Works even with IP like `http://192.168.x.x:5678`
⚠ Not safe for production

---

### 🥉 Option 3: Setup HTTPS (Best for production)

* Use reverse proxy like:

  * nginx
  * Caddy
* Add SSL (Let’s Encrypt)

✔ Proper fix
✔ Needed for deployment
❗ Overkill for local use

---

### ⚠ Safari-specific issue

If you’re using **Safari**, even `localhost` can sometimes fail.

👉 Solutions:

* Switch to:

  * Chrome / Brave / Edge
* OR disable secure cookie (Option 2)

---

If you want next step, I can help you:

* Run n8n in background (so it doesn’t stop)
* Setup with Docker
* Or expose it publicly with HTTPS 🚀
