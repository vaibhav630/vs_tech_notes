# Connect Ollama to n8n

Since n8n doesn’t have a native Ollama node yet, we’ll use **HTTP Request node**.

### Configure HTTP Request node:

* **Method:** POST

* **URL:**

  ```
  http://localhost:11434/api/generate
  ```

* **Headers:**

```json
Content-Type: application/json
```

* **Body (RAW JSON):**

```json
{
  "model": "llama3",
  "prompt": "Write a short motivational quote",
  "stream": false
}
```

# Process Response

Ollama returns JSON like:

```json
{
  "response": "Your generated text..."
}
```

In n8n:

* Use a **Set node** or **Function node**
* Extract:

```javascript
{{$json["response"]}}
```

---

# Example Workflow Idea

**Webhook → Ollama → Response**

1. Webhook node (input text)
2. HTTP Request (send to Ollama)
3. Respond node (return AI output)

---

# ⚠️ Common Issues (Important)

### 1. Secure Cookie Error (you saw this)

If accessing via IP or HTTP:

Fix:

```bash
export N8N_SECURE_COOKIE=false
```

OR use:

```
http://localhost:5678
```

---

### 2. Problem in node ‘HTTP Request‘ The service refused the connection - perhaps it is offline

Even locally, n8n sometimes fails with localhost due to how Node.js resolves networking internally.

✅ Fix: Change URL in HTTP node:

Instead of:
```
http://localhost:11434/api/generate
```
Use:
```
http://127.0.0.1:11434/api/generate
```
🧪 Why this works
- localhost → resolves via DNS → can behave differently inside Node (n8n)
- 127.0.0.1 → direct loopback → always reliable

---

### 3. Ollama not responding

Check:

```bash
ollama list
```

Ensure:

* Model is downloaded
* Server is running

---

### 4. Streaming issues

Set:

```json
"stream" : false  
```

Otherwise n8n can’t parse chunks properly.

---



