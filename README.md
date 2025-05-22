# Multi-Source-Research-Agent
# 📚 AI Research Agent

**Multi-source Research Assistant** powered by **LangChain**, **LLMs**, and **Streamlit**.  
Ask any research question — it pulls insights from PDFs, Wikipedia, and YouTube to generate a smart, concise answer with citations.

---

## 🚀 Features

- ✅ Accepts a user query for any research topic  
- 📄 Extracts content from uploaded **PDFs**  
- 🌐 Gathers information from **Wikipedia**  
- 📺 Transcribes and analyzes **YouTube** videos  
- 🧠 Uses **LLMs via Hugging Face** for intelligent summarization  
- 📌 Provides answers with **source citations**  

---

## 🧠 Powered By

- **LangChain** – Document loaders, prompt chaining, RAG
- **Hugging Face** – Mistral-7B-Instruct via HuggingFaceHub
- **FAISS** – Vector store for similarity search
- **Streamlit** – Web-based interface
- **PyMuPDF** – PDF loader
- **YouTubeTranscriptAPI** – Extracts transcripts
- **WikipediaLoader** – Fetches context from Wikipedia

---

## 📦 Installation

1. Clone this repo
   
  git clone https://github.com/yourusername/Multi-Source-Research-Agent.git
  
  cd Multi-Source-Research-Agent

2. Create .env file
   
  cp .env.example .env

  Then fill in:
  
  HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

3. Install dependencies

  pip install -r requirements.txt

4.Run the app (in Colab or locally)

  streamlit run app.py
  
  If using Google Colab, use pyngrok to expose the port.

---
## 💡 Example Use Case

**Query:**  
`"Explain LangChain and its applications"`

**Sources Used:**

- ✅ Wikipedia page on LangChain  
- ✅ Uploaded PDF (LangChain whitepaper)  
- ✅ YouTube video transcript: *LangChain for Developers*

**Output:**  
A short, clear summary citing each source with references like `[1]`, `[2]`, etc.

---
## 📁 Project Structure

Multi-Source-Research-Agent/

├── app.py

├── requirements.txt

├── README.md

├── assets/

│   └── demo_screenshot.png

└── notebooks/

│   └── Multi_Source_Research.ipynb
  
---

## 📸 Screenshot

![IMG_20250521_214447.jpg](https://github.com/user-attachments/assets/d5d2600c-c7ba-4493-9c25-f242cdc1bf92)
![IMG_20250521_214510](https://github.com/user-attachments/assets/98209ab7-bb87-40eb-80e4-43bf119a442c)

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)  
- [Hugging Face](https://huggingface.co/)  
- [Streamlit](https://streamlit.io/)  
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)  

---

## ✍️ Author

**Asgarali Malpara**  
GitHub: [@asgarali429](https://github.com/asgarali429)
