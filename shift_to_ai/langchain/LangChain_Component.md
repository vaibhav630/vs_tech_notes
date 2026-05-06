## 🧩 Core Components of LangChain

LangChain has **6 main components**:

1. Models
2. Prompts
3. Chains
4. Memory
5. Indexes
6. Agents

---

## 1️⃣ Models

### 📖 Definition:

* Interface to interact with AI models.

### ❗ Problem Solved:

* Different providers (OpenAI, Anthropic, etc.) have **different APIs**
* LangChain standardizes interaction

### 🔑 Types of Models:

* **Language Models (LLMs)**

  * Input: Text → Output: Text
  * Example: Chatbots

* **Embedding Models**

  * Input: Text → Output: Vector
  * Used for semantic search

### ✅ Benefits:

* Easy switching between providers
* Standardized response handling

---

## 2️⃣ Prompts

### 📖 Definition:

* Input given to an LLM

### ⚠️ Importance:

* Output is highly dependent on prompt design

### 🧠 Prompt Techniques:

#### 🔹 Dynamic Prompts

```
Summarize {topic} in {tone}
```

#### 🔹 Role-based Prompts

```
You are an experienced {profession}
Explain {topic}
```

#### 🔹 Few-shot Prompting

* Provide examples before asking a question

### 💼 Field:

* Prompt Engineering (growing domain)

---

## 3️⃣ Chains

### 📖 Definition:

* Used to build **pipelines of operations**

### 🔁 Key Idea:

* Output of one step → Input of next step (automatic)

### 🧱 Example:

1. Translate English → Hindi
2. Summarize Hindi text

### 🔄 Types of Chains:

#### 🔹 Sequential Chain

* Step-by-step execution

#### 🔹 Parallel Chain

* Multiple LLMs run simultaneously

#### 🔹 Conditional Chain

* Flow depends on conditions

---

## 4️⃣ Indexes

### 📖 Definition:

* Connect LLMs with **external data sources**

### 📦 Components:

1. Document Loader
2. Text Splitter
3. Vector Store
4. Retriever

### 🔁 Workflow:

1. Load documents
2. Split into chunks
3. Convert into embeddings
4. Store in vector DB
5. Retrieve relevant data for queries

### 🎯 Use Case:

* Chat with PDFs, company data, websites

---

## 5️⃣ Memory

### 📖 Definition:

* Enables LLMs to **remember past interactions**

### ⚠️ Problem:

* LLM APIs are **stateless**

### 🧠 Types of Memory:

#### 🔹 Conversation Buffer

* Stores entire chat

#### 🔹 Buffer Window

* Stores last N interactions

#### 🔹 Summarized Memory

* Stores summary of conversation

#### 🔹 Custom Memory

* Stores specific user data/preferences

---

## 6️⃣ Agents

### 📖 Definition:

* AI systems that can **perform actions**, not just respond

### 🤖 Difference from Chatbots:

| Chatbot           | Agent                 |
| ----------------- | --------------------- |
| Only responds     | Can take actions      |
| No tools          | Uses tools            |
| Limited reasoning | Has reasoning ability |

### ⚙️ Capabilities:

* Reasoning (breaking tasks into steps)
* Tool usage (APIs, calculators, etc.)

### 🧠 Example Flow:

1. Understand query
2. Identify required tools
3. Execute actions
4. Return result

---

## 🧠 Key Takeaways

* LangChain simplifies **LLM application development**
* Core strength lies in:

  * Standardization
  * Pipeline creation
  * External data integration
* Understanding these 6 components = **strong foundation**

---

## 📍 Conclusion

* This is a **high-level overview**
* Future learning should dive deep into each component
* Start with **Models → Prompts → Chains → Indexes → Memory → Agents**

---

If you want, I can also:

* Convert this into **short revision notes (1-page)**
* Or create a **visual diagram / cheat sheet** for quick recall
