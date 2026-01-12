import streamlit as st
from src.search import RAGSearch

st.set_page_config(page_title="DocSearch", page_icon="📄", layout="centered")
st.markdown(
    """
    <style>
    header [aria-label="Deploy"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)





# ---- Title + description with inline links ----
st.markdown(
    """
# 📄 DocSearch  
Built with **RAG + LLM** on documents: 
**[Embeddings](https://web.stanford.edu/~jurafsky/slp3/5.pdf)** ·
**[RAG Survey](https://arxiv.org/pdf/2312.10997)** ·
**[LangChain](https://www.turing.ac.uk/sites/default/files/2024-11/langchain.pdf)**
"""
)


# ---- App logic ----
@st.cache_resource
def _init():
    with st.spinner("Loading search engine..."):
        return RAGSearch(persist_dir="faiss_store")

rag = _init()


query = st.text_input(
    "Ask a question: ",
    placeholder="e.g., What are the main limitations of Naive RAG?"
)

top_k = st.slider("Top K results", 1, 10, 3)

if st.button("Search"):
    if not query.strip():
        st.warning("Type a question first.")
    else:
        with st.spinner("Searching..."):
            answer = rag.search_and_summarize(query, top_k=top_k)
        st.subheader("Answer")
        st.write(answer)
