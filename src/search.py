import os
from dotenv import load_dotenv
from src.vectorstore import FaissVectorStore
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from src.data_loader import load_all_documents

load_dotenv()

class RAGSearch:
    def __init__(self, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2", llm_model: str = "llama-3.1-8b-instant"):
        self.vectorstore = FaissVectorStore(persist_dir, embedding_model)
        # Load or build vectorstore
        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            from src.data_loader import load_all_documents
            docs = load_all_documents("data")
            self.vectorstore.build_from_documents(docs)
        else:
            self.vectorstore.load()
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("Missing GROQ_API_KEY. Set it in .env or your` deployment secrets.")

        llm_model = os.getenv("GROQ_MODEL", llm_model)
        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name=llm_model,
            temperature=0.2,
            max_tokens=800
        )


        print(f"[INFO] Groq LLM initialized: {llm_model}")

    def search_and_summarize(self, query: str, top_k: int = 5) -> str:
        results = self.vectorstore.query(query, top_k=top_k)
        texts = [r["metadata"].get("text", "") for r in results if r.get("metadata")]
        reference = "\n\n".join([t for t in texts if t.strip()])

        if not reference.strip():
            return "No relevant documents found."

        system = SystemMessage(content="""
        You are a strict question-answering assistant.

        You MUST follow these rules:
        - Your first word must be part of the answer (no preface like “The provided…”).
        - Use ONLY the provided reference text.
        - If the reference does not contain the answer, output EXACTLY:
        I don't know based on the provided documents.
        - Do NOT explain what the reference is about.
        - Do NOT mention the words: context, reference, excerpts, documents, query.
        """.strip())

        user = HumanMessage(content=f"""
        Question: {query}

        Reference text:
        {reference}
        """.strip())

        response = self.llm.invoke([system, user])
        return response.content



# Example usage
if __name__ == "__main__":
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
