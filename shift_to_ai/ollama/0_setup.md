Using Ollama Locally

---

# Install Ollama

```bash
brew install ollama
```

# Start Ollama:

```bash
ollama serve
```

Open a new terminal and Pull a model (example: Llama 3):

```bash
ollama pull llama3
```

Test it:

```bash
ollama run llama3
```

# Verify Ollama API

Ollama runs a local API by default:

```
http://localhost:11434
```

Test via curl:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Hello"
}'
```

