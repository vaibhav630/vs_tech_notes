# on pulling where the model is getting stored in disk, can I see in finder app

---

When you pull a model using Ollama, it **does get stored on your disk**, but it’s kept in a hidden system folder.


# 📂 Where Ollama stores models on macOS

By default, models are stored here:

```
~/.ollama/models
```

👉 Expanded path:

```
/Users/<your-username>/.ollama/models
```

---

# 👀 Can you see it in Finder?

Yes — but it’s **hidden by default**.

## ✅ Method 1: Use “Go to Folder” (easiest)

1. Open Finder
2. Press **Cmd + Shift + G**
3. Paste:

```
~/.ollama
```

4. Press Enter

👉 You’ll now see the folder, including:

* `models/` (actual model files)
* blobs (large binary chunks)

---

## ✅ Method 2: Show hidden files

1. Open Finder
2. Go to your home directory (`/Users/yourname`)
3. Press:

```
Cmd + Shift + .
```

👉 This toggles hidden files
Now you’ll see `.ollama`

---

# 📦 What’s inside the models folder?

You won’t see clean names like “llama3.gguf”

Instead, you’ll see:

* `blobs/` → actual model data (large files)
* `manifests/` → metadata

👉 Ollama manages mapping internally, so filenames look cryptic.

---

# ⚠️ Important warning

* ❌ Don’t manually edit/delete files inside `.ollama`
* ✅ Always use:

```bash
ollama rm llama3
```

Otherwise, you can break model references.

---

# 🧠 Pro tip (advanced)

If you ever want to **change storage location** (e.g., external SSD):

You can set environment variable:

```bash
OLLAMA_MODELS=/path/to/your/folder
```

---

# 🔍 Quick summary

* Yes, models are stored locally ✅
* Location: `~/.ollama/models`
* Hidden → use Finder “Go to Folder”
* Managed by Ollama → don’t manually touch