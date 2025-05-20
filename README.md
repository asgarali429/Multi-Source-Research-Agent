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

💡 Example Use Case
Query:
"Explain LangChain and its applications"

Sources Used:

✅ Wikipedia page on LangChain

✅ Uploaded PDF (LangChain whitepaper)

✅ YouTube video transcript: LangChain for Developers

Output:
A short, clear summary citing each source with a reference like [1], [2], etc.

📁 Project Structure
Copy
Edit
AI-Research-Agent/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── assets/
│   └── demo_screenshot.png
└── notebooks/
📸 Screenshot

📝 License
This project is licensed under the MIT License.

🙏 Acknowledgements
LangChain

Hugging Face

Streamlit

YouTube Transcript API

✍️ Author
Your Name
GitHub: @yourusername


















ChatGPT c