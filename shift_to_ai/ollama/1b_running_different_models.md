# 🧠 1. How to decide which model to pull

There’s no single “best” model — it depends on your **use case + hardware**.

## 🔑 A. Based on your use case

| Use case                 | Recommended models |
| ------------------------ | ------------------ |
| General chat / coding    | Llama 3            |
| Fast + lightweight       | Mistral            |
| Best reasoning (heavier) | Mixtral            |
| Code-heavy tasks         | Code Llama         |

---

## 💻 B. Based on your system (VERY IMPORTANT)

Since you're on a Mac:

| RAM    | What you should run            |
| ------ | ------------------------------ |
| 8 GB   | 7B models (mistral, llama3:8b) |
| 16 GB  | 7B–13B models                  |
| 32 GB+ | 13B–70B (if patient 😄)        |

👉 Rule:

* Smaller model = faster
* Bigger model = smarter (but slower)

---

## 🚀 Safe starting point (recommended)

Start with:

```bash
ollama pull llama3
```

This gives you:

* Good balance of **speed + intelligence**
* Works well with tools like n8n

---

# 🔄 2. How to change the model later

## 📦 Pull multiple models (recommended)

You can keep many models locally:

```bash
ollama pull mistral
ollama pull llama3
ollama pull codellama
```

Then just switch anytime when running.

## ▶️ Run a different model

```bash
ollama run mistral
```

or

```bash
ollama run llama3
```

---

# 🔍 Bonus: How to explore models

Run:

```bash
ollama list
```

Shows all downloaded models.

---