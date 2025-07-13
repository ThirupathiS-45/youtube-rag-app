# rag_utils.py

from dotenv import load_dotenv
load_dotenv()

import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    return None

def fetch_transcript(video_url):
    video_id = get_video_id(video_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([t['text'] for t in transcript]), video_id

def create_or_load_vectorstore(transcript_text, video_id):
    persist_dir = f"chroma_db/{video_id}"
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # If Chroma DB already exists for this video
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    else:
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_text(transcript_text)
        vectordb = Chroma.from_texts(chunks, embedding=embeddings, persist_directory=persist_dir)
        vectordb.persist()
    return vectordb

def setup_qa(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    return qa_chain
