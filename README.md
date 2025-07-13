# 🤖 QUERY WAVE – AI-Powered YouTube Q&A Assistant

**QUERY WAVE** is an AI-powered chatbot that transforms YouTube videos into interactive conversations using **Retrieval-Augmented Generation (RAG)**.  
Just paste a YouTube URL, and ask questions directly about the video — no need to watch it fully!

---

## 🚀 Features

- 🔗 Paste any YouTube video URL
- 📄 Automatically extracts transcript using YouTube Transcript API
- 🧠 Splits and embeds content using LangChain + Google Gemini Embeddings
- 📦 Stores vector embeddings locally using ChromaDB
- 💬 Uses Gemini 1.5 Flash + LangChain for real-time Q&A
- 💾 Maintains session-based chat memory for multi-turn conversations
- 🖥️ Built with Streamlit (sidebar input + chatbot interface)

---

## ⚙️ Tech Stack

- **LangChain** – RAG pipeline + semantic search
- **Google Gemini 1.5 Flash** – Fast, intelligent LLM responses
- **ChromaDB** – Local vector store for similarity search
- **YouTube Transcript API** – Fetches full video text
- **Streamlit** – Interactive web-based UI

---

## 🧪 How It Works

1. User pastes a YouTube video URL.
2. Transcript is extracted using the YouTube Transcript API.
3. Transcript is split into chunks using LangChain.
4. Each chunk is embedded using Google Generative AI Embeddings.
5. Embeddings are stored in a local ChromaDB vector store.
6. User asks a question → LangChain performs semantic search.
7. Gemini 1.5 Flash uses relevant chunks to answer accurately.

---

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/ThirupathiS-45/youtube-rag-app.git
cd youtube-rag-app

# Create a virtual environment
python -m venv .venv

# Activate it
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

---
```markdown
## 🔐 Setup Environment Variables

Create a `.env` file in the root directory and add your Google API key:

```ini
GOOGLE_API_KEY=your_google_generative_ai_api_key
```

🔑 You can get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🗂️ Folder Structure

```bash
youtube-rag-app/
├── app.py              # Main Streamlit frontend
├── rag_utils.py        # RAG logic (transcript → embedding → QA)
├── .env                # Your API key (keep it secret!)
├── .gitignore          # Ignore env & venv folders
├── requirements.txt    # Python dependencies
└── README.md           # This documentation
```

---

## 📄 .gitignore

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

---

## 🤝 Let’s Connect

- 💼 [LinkedIn – Thirupathi S](https://www.linkedin.com/in/thirupathis/)
- 🌟 Star this repo if you found it helpful!
```
