Here are your **clean, structured notes in `.md` format (English)** based on the provided transcript, with **code examples included** 👇

---

# 📘 LangChain Models – Notes

## 🔹 What is Model Component in LangChain?

* The **Model component** in LangChain provides a **common interface** to interact with different AI models.
* It helps developers avoid dealing with different APIs for each provider.

### ✅ Key Idea:

> A unified interface to interact with multiple AI models.

---

## 🔹 Types of Models in LangChain

LangChain supports **2 types of models**:

### 1. Language Models (LLMs)

* Input → Text
* Output → Text

**Example:**

```text
Input: What is the capital of India?
Output: New Delhi
```

📌 Used for:

* Chatbots
* Text generation
* Summarization
* Code generation

---

### 2. Embedding Models

* Input → Text
* Output → Vector (numbers)

📌 Used for:

* Semantic search
* RAG (Retrieval-Augmented Generation)
* Similarity comparison

---

## 🔹 Types of Language Models

### 1. LLMs (Traditional)

* Input: String
* Output: String
* General purpose
* No conversation memory

### 2. Chat Models (Modern – Recommended)

* Input: List of messages
* Output: Structured response
* Supports:

  * Conversation history
  * Role-based prompts (system, user)

📌 **Recommendation:** Use Chat Models instead of LLMs

---

## 🔹 Project Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Using OpenAI LLM in LangChain

```python
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("What is the capital of India?")

print(result)
```

---

## 🔹 Using Chat Model (OpenAI)

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")

result = model.invoke("What is the capital of India?")

print(result.content)
```

📌 Difference:

* LLM → returns plain string
* Chat Model → returns object (`result.content`)

---

## 🔹 Important Parameters

### 1. Temperature (Creativity Control)

| Value Range | Behavior      |
| ----------- | ------------- |
| 0 – 0.3     | Deterministic |
| 0.5 – 0.7   | Balanced      |
| 1+          | Creative      |

```python
model = ChatOpenAI(model="gpt-4", temperature=0.7)
```

---

### 2. Max Tokens (Response Length)

```python
model = ChatOpenAI(model="gpt-4", max_tokens=50)
```

📌 Controls cost + output length

---

## 🔹 Using Anthropic (Claude)

```python
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3.5-sonnet")

result = model.invoke("What is the capital of India?")

print(result.content)
```

---

## 🔹 Using Google Gemini

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

result = model.invoke("What is the capital of India?")

print(result.content)
```

---

## 🔹 Open Source Models

### 📌 What are Open Source Models?

* Free to use
* Can run locally
* Fully customizable

### Examples:

* LLaMA
* Mistral
* Falcon
* Bloom

---

## 🔹 Using Hugging Face API

```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result.content)
```

---

## 🔹 Open Source vs Closed Source

| Feature       | Open Source | Closed Source |
| ------------- | ----------- | ------------- |
| Cost          | Free        | Paid          |
| Control       | Full        | Limited       |
| Privacy       | High        | Low           |
| Customization | High        | Limited       |

---

## 🔹 Key Takeaways

* LangChain provides a **unified interface** for AI models.
* Two main model types:

  * Language Models
  * Embedding Models
* Chat Models are the **future (preferred over LLMs)**.
* You can use:

  * OpenAI
  * Anthropic
  * Google
  * Hugging Face
* Open source models give **more control but require resources**.

---

## 🔹 Flow Summary

```text
User Input → LangChain Model Interface → AI Model → Response
```

---

## 📌 Reference

Content derived from your uploaded transcript: 

---

If you want next step, I can:

* Convert this into **interview notes (Q&A format)**
* Or create a **cheat sheet for quick revision**
* Or help you build a **real mini project (RAG / chatbot)** 🚀
