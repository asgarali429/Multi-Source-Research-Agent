# Multi-Source-Research-Agent
# 📚 AI Research Agent

**Multi-source Research Assistant** powered by **LangChain**, **LLMs**, and **Streamlit**.  
Ask any research question — it pulls insights from PDFs, Wikipedia, and YouTube to generate a smart, concise answer with citations.

![Demo](assets/demo_screenshot.png)

---

## 🚀 Features

- ✅ Accepts a research question from the user
- 📄 Loads and processes **PDFs**
- 🌐 Gathers context from **Wikipedia**
- 📺 Extracts **YouTube transcripts**
- 🤖 Generates answers using **Hugging Face LLMs**
- 📌 Outputs with **source citations** (Wikipedia, YouTube, PDF)

---

## 🧠 Powered By

- **LangChain** – For document loading, RAG, prompt chains
- **Hugging Face** – Inference with `Mistral-7B-Instruct` via HuggingFaceHub
- **FAISS** – For embedding search
- **Streamlit** – Frontend web interface
- **PyMuPDF** – PDF parsing
- **YouTubeTranscriptAPI** – YouTube subtitle extraction
- **WikipediaLoader** – Built-in LangChain loader

---

## 📦 Installation

1. **Clone this repo**

```bash
git clone https://github.com/yourusername/AI-Research-Agent.git
cd AI-Research-Agent
