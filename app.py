import streamlit as st
from langchain_community.document_loaders import WikipediaLoader, PyMuPDFLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import re
import tempfile
import os
from dotenv import load_dotenv
import streamlit as st
from pyngrok import ngrok

# Load API token from .env file
load_dotenv()
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# --- UI ---
st.set_page_config(page_title="AI Research Assistant", layout="centered")
st.title("📚 AI Research Assistant")

query = st.text_input("🔍 Enter your research question:")
uploaded_pdf = st.file_uploader("📄 Upload a PDF (optional)", type="pdf")
youtube_url = st.text_input("▶️ Paste YouTube URL (optional)")
run_button = st.button("Get Answer")

if run_button and query:
    with st.spinner("🔍 Processing..."):

        # Loaders
        docs = []

        # Wikipedia
        wiki_loader = WikipediaLoader(query=query, load_max_docs=17)
        wiki_docs = wiki_loader.load()
        for doc in wiki_docs:
            doc.metadata["source"] = f"Wikipedia: {doc.metadata.get('title', 'Unknown')}"
        docs.extend(wiki_docs)

        # PDF
        if uploaded_pdf:
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_pdf.read())
                    tmp_path = tmp.name
                pdf_loader = PyMuPDFLoader(tmp_path)
                pdf_docs = pdf_loader.load()
                for doc in pdf_docs:
                    doc.metadata["source"] = f"PDF: {uploaded_pdf.name}"
                docs.extend(pdf_docs)
                os.unlink(tmp_path)
                st.success("✅ PDF loaded")
            except Exception as e:
                st.warning(f"⚠️ PDF loading failed: {e}")

        # YouTube
        if youtube_url:
            match = re.search(r"(?:v=|youtu.be/)([\w-]+)", youtube_url)
            if match:
                video_id = match.group(1)
                try:
                    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
                    transcript = " ".join(chunk["text"] for chunk in transcript_list)
                    doc = Document(page_content=transcript, metadata={"source": f"YouTube: {youtube_url}"})
                    docs.append(doc)
                    st.success("✅ YouTube transcript loaded")
                except (TranscriptsDisabled, NoTranscriptFound):
                    st.warning("⚠️ No usable English transcript found. Skipping video.")
                except Exception as e:
                    st.warning(f"⚠️ Error fetching/parsing transcript: {e}")
            else:
                st.warning("⚠️ Invalid YouTube URL")

        # Text Splitting
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        split_docs = text_splitter.split_documents(docs[:5])
        st.info(f"🔹 Total Chunks: {len(split_docs)}")

        # Embeddings & Vector Store
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectors = FAISS.from_documents(split_docs, embeddings)
        retriever = vectors.as_retriever(search_type="similarity", k=5)

        llm = HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.3",
            task="text-generation",
            huggingfacehub_api_token=api_key
        )
        model = ChatHuggingFace(llm=llm)

        # Prompt Template
        prompt = PromptTemplate(
            template="""
You are a helpful assistant.
Use the context below to answer the query, and reference sources using [number] format.
If the context is insufficient, just say you don't know.

{context}

Query: {query}
Answer:
""",
            input_variables=["context", "query"]
        )

        # Format for source referencing
        def format_docs_with_citations(docs):
            formatted = []
            for i, doc in enumerate(docs, 1):
                source = doc.metadata.get("source", "Unknown source")
                formatted.append(f"[{i}] {doc.page_content}\n(Source: {source})")
            return "\n\n".join(formatted)

        # Chain
        parallel_chain = RunnableParallel({
            "context": retriever | RunnableLambda(format_docs_with_citations),
            "query": RunnablePassthrough()
        })
        final_chain = parallel_chain | prompt | model | StrOutputParser()

        # Run the chain
        answer = final_chain.invoke(query)
        st.success("✅ Answer Generated:")
        st.write(answer)
