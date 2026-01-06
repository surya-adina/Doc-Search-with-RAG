import os
from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":
    persist_dir = "faiss_store"
    faiss_path = os.path.join(persist_dir, "faiss.index")
    meta_path = os.path.join(persist_dir, "metadata.pkl")

    # Build once if missing, else reuse
    if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
        docs = load_all_documents("data")
        store = FaissVectorStore(persist_dir)
        store.build_from_documents(docs)

    # Run search (this will load the existing store)
    rag_search = RAGSearch(persist_dir=persist_dir)

    query = "What are the main limitations of Naive RAG discussed in the survey?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
