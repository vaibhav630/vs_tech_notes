When I pull models, how much memory of my local system gets occupied
---
There are **two types of “memory” involved**, and people often confuse them:

# 💾 1. Disk space (storage) — when you *pull* a model

This is the space used on your **hard drive / SSD**.

## 📦 Typical model sizes

| Model        | Size on disk |
| ------------ | ------------ |
| Mistral      | ~4–5 GB      |
| Llama 3 (8B) | ~4–6 GB      |
| Llama 3      | ~35–40 GB 😳 |
| Mixtral      | ~25–30 GB    |

So when you run:

```bash
ollama pull llama3
```

You’re downloading ~5 GB to your disk.

---

# ⚡ 2. RAM usage — when you *run* a model

This is what matters for performance.

| Model          | RAM needed (approx)                |
| -------------- | ---------------------------------- |
| 7B / 8B models | 6–8 GB RAM                         |
| 13B models     | 10–16 GB RAM                       |
| 70B models     | 40+ GB RAM (not practical locally) |

👉 Important:

* If RAM is insufficient → system becomes **slow or crashes**
* Ollama may use **swap (disk)** → very slow

---

# 🧠 Simple analogy

* **Pulling model** = installing an app (uses storage)
* **Running model** = opening the app (uses RAM)

---

# 📊 Example for your Mac

Let’s say you:

```bash
ollama pull llama3
ollama pull mistral
```

### Disk usage:

* ~5 GB (llama3)
* ~4 GB (mistral)
  👉 Total ≈ **9 GB used**

### RAM usage:

* Only **one model runs at a time**
* So RAM usage = ~6–8 GB (not 9+ GB)

---

# 🔍 Check your usage

### See downloaded models:

```bash
ollama list
```

### Delete a model:

```bash
ollama rm mistral
```

---
