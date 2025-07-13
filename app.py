# app.py

import streamlit as st
from rag_utils import fetch_transcript, create_or_load_vectorstore, setup_qa

# App config
st.set_page_config(page_title="🎥 QUERY WAVE", layout="wide")

# Sidebar for video input
with st.sidebar:
    st.title("🎬 Load YouTube Video")
    st.markdown("Paste the video URL and build the knowledge base.")
    video_url = st.text_input("🔗 YouTube Video URL")

    if video_url and (
        "qa_chain" not in st.session_state or st.session_state.get("video_url") != video_url
    ):
        with st.spinner("🔄 Processing video transcript and embeddings..."):
            try:
                transcript, video_id = fetch_transcript(video_url)
                vectordb = create_or_load_vectorstore(transcript, video_id)
                qa_chain = setup_qa(vectordb)

                # Save to session
                st.session_state.qa_chain = qa_chain
                st.session_state.video_url = video_url
                st.session_state.chat_history = []
                st.success("✅ Video ready! Start chatting in the main window.")
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Main chatbot interface
# Main chatbot interface
st.markdown("<h1 style='text-align: center;'>🤖 QUERY WAVE</h1>", unsafe_allow_html=True)


# Check if knowledge base is ready
if "qa_chain" in st.session_state:
    qa_chain = st.session_state.qa_chain

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(msg["user"])
        with st.chat_message("assistant"):
            st.markdown(msg["bot"])

    # New message input
    user_query = st.chat_input("Ask a question about the video...")

    if user_query:
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.spinner("💭 Wave is thinking..."):
            response = qa_chain.invoke(user_query)
            answer = response["result"]

        with st.chat_message("assistant"):
            st.markdown(answer)

        # Save to history
        st.session_state.chat_history.append({"user": user_query, "bot": answer})
else:
    st.info("📌 Please load a YouTube video from the sidebar to begin.")
