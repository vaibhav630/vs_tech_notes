Great choice—**n8n** is super powerful for automation (like Zapier but self-hosted + dev-friendly)

---

# ✅ Option 1: Install n8n using Node.js (Recommended for you)

Since you're already working with Node.js + NVM, this is the cleanest way.

## 1️⃣ Install n8n globally

Open Terminal and run:

```bash
npm install -g n8n
```

---

## 2️⃣ Start n8n

```bash
n8n
```

You should see something like:

```
Editor is now accessible via:
http://localhost:5678
```

👉 Open this in your browser:

```
http://localhost:5678
```

---

## 3️⃣ Done 🎉

You now have n8n running locally.

---

# 🧠 Optional (but IMPORTANT for real usage)

## Enable basic authentication (security)

```bash
export N8N_BASIC_AUTH_ACTIVE=true
export N8N_BASIC_AUTH_USER=admin
export N8N_BASIC_AUTH_PASSWORD=yourpassword
n8n
```

---

# ✅ Option 2: Run n8n with npx (no install)

If you don’t want global install:

```bash
npx n8n
```

---

# 🐳 Option 3: Using Docker (best for production later)

If you plan long-term usage:

```bash
docker run -it --rm \
  -p 5678:5678 \
  n8nio/n8n
```

---

# ⚠️ Common Issues

### 1. Command not found: n8n

Fix:

```bash
npm install -g n8n
```

---

### 2. Permission issues

Avoid `sudo`, instead fix npm permissions or use nvm (which you already are 👍)

---

### 3. Port already in use

```bash
n8n --port 5679
```

---
