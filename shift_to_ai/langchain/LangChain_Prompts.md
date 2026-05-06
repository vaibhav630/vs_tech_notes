Here are your **clean, structured Markdown notes (.md format)** based on the provided transcript 👇

---

# 📘 LangChain Prompts – Notes

## 📌 1. Introduction to Prompts

* A **prompt** is the input/message sent to an LLM.
* Example:

```python
model.invoke("Write a 5 line poem on cricket")
```

* Prompts can be:

  * Text (most common)
  * Image
  * Audio
  * Video (multimodal prompts)

👉 In practice, **99% use cases are text-based prompts**.

---

## ⚠️ Importance of Prompts

* LLM output is **highly sensitive** to prompts.
* Small changes → completely different outputs.
* This led to a new field:
  👉 **Prompt Engineering**

---

## 🌡️ Temperature Parameter (Correction)

* Controls randomness/creativity.

| Temperature | Behavior                               |
| ----------- | -------------------------------------- |
| 0           | Deterministic (same output every time) |
| ~1.5–2      | Creative (different outputs each time) |

```python
model = ChatOpenAI(temperature=0)
```

---

## 🧱 Static vs Dynamic Prompts

### ❌ Static Prompt

```python
model.invoke("Summarize Attention is All You Need paper")
```

* Written directly in code
* User has full control → inconsistent results
* High chance of errors

---

### ✅ Dynamic Prompt (Recommended)

* Use **templates with placeholders**

Example template:

```
Please summarize the research paper titled {paper_input}
Style: {style_input}
Length: {length_input}
```

👉 Values are filled at runtime.

---

## 🧩 PromptTemplate in LangChain

### ✅ Basic Usage

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Summarize {paper} in {style} style",
    input_variables=["paper", "style"]
)

prompt = template.invoke({
    "paper": "Attention is All You Need",
    "style": "simple"
})
```

---

## 🤔 Why Not Use f-strings?

You *can* use f-strings, but PromptTemplate is better because:

### 1. ✅ Validation

* Detects missing variables

```python
PromptTemplate(..., validate_template=True)
```

---

### 2. ♻️ Reusability

* Save/load templates

```python
template.save("template.json")
```

```python
from langchain_core.prompts import load_prompt
template = load_prompt("template.json")
```

---

### 3. 🔗 Works with Chains

```python
chain = template | model
result = chain.invoke({
    "paper": "...",
    "style": "simple"
})
```

👉 Only one `.invoke()` needed

---

## 💬 Building a Simple Chatbot

### Basic Version (No Memory)

```python
while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    result = model.invoke(user_input)
    print("AI:", result.content)
```

---

### ❌ Problem

* No context awareness

Example:

```
User: Which is greater 2 or 0?
User: Multiply the bigger number by 10
```

❌ Wrong output (no memory)

---

## 🧠 Chat History (Memory)

### ✅ Solution: Maintain chat history

```python
chat_history = []

chat_history.append(user_input)
result = model.invoke(chat_history)
chat_history.append(result.content)
```

---

## 📩 Message Types in LangChain

LangChain defines **3 message types**:

### 1. SystemMessage

* Sets behavior

```python
SystemMessage(content="You are a helpful assistant")
```

---

### 2. HumanMessage

* User input

```python
HumanMessage(content="Tell me about LangChain")
```

---

### 3. AIMessage

* Model response

```python
AIMessage(content="LangChain is a framework...")
```

---

### ✅ Example

```python
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are helpful"),
    HumanMessage(content="Explain LangChain")
]

result = model.invoke(messages)
```

---

## 🔄 Chat History with Roles

```python
chat_history = [
    SystemMessage(content="You are helpful"),
    HumanMessage(content="Hi"),
    AIMessage(content="Hello!")
]
```

👉 Important: Always track **who said what**

---

## 🧩 ChatPromptTemplate

Used for **dynamic multi-message prompts**

### Example:

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a {domain} expert"),
    ("human", "Explain {topic}")
])

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "Duckworth Lewis method"
})
```

---

## ⚠️ Important Note

❌ This may not work properly:

```python
SystemMessage(...)
```

✅ Use tuple format:

```python
("system", "You are a {domain} expert")
```

---

## 📌 Message Placeholder

### Purpose:

* Insert **chat history dynamically**

### Definition:

> Special placeholder to inject past messages into a prompt 

---

### Use Case:

* Customer support chatbot
* Resume conversation from previous session

---

### Example Flow:

1. Store chat history (DB/file)
2. Load history
3. Insert into prompt using placeholder

---

## 🔁 Two Ways to Use `.invoke()`

### 1. Single Message

* For one-time queries

```python
model.invoke("Summarize this")
```

---

### 2. List of Messages

* For conversations

```python
model.invoke(messages)
```

---

## 🧠 Key Takeaways

* Prompts = Core of LLM behavior
* Prefer **dynamic prompts** over static
* Use:

  * `PromptTemplate` → single prompt
  * `ChatPromptTemplate` → conversations
* Maintain **chat history with roles**
* Use **message placeholders** for memory
* Avoid raw f-strings in production

---

## 🚀 What’s Next

* Chains in LangChain
* Memory modules
* Advanced prompt engineering

---

If you want, I can next:
👉 Convert this into **interview notes (1-pager)**
👉 Or create **revision cheatsheet + diagrams**
