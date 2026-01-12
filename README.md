<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="Doc-Search-with-RAG.png" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# DOC-SEARCH-WITH-RAG

<em>Unlock Knowledge Instantly with Smarter Search</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/surya-adina/Doc-Search-with-RAG?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/surya-adina/Doc-Search-with-RAG?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/surya-adina/Doc-Search-with-RAG?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=flat&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/LangChain-1C3C3C.svg?style=flat&logo=LangChain&logoColor=white" alt="LangChain">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/uv-DE5FE9.svg?style=flat&logo=uv&logoColor=white" alt="uv">

</div>
<br>

---

## 📄 Table of Contents

- [Overview](#-overview)
- [Getting Started](#-getting-started)
    - [Prerequisites](#-prerequisites)
    - [Installation](#-installation)
    - [Usage](#-usage)
    - [Testing](#-testing)
- [Features](#-features)
-  [Live Demo](#-live-demo)
- [Project Structure](#-project-structure)
    - [Project Index](#-project-index)

---

## ✨ Overview

Doc-Search-with-RAG is an open-source developer tool that combines advanced NLP, vector similarity search, and interactive interfaces to enable efficient document ingestion, semantic search, and knowledge retrieval. It streamlines building intelligent information systems capable of summarizing and answering questions based on large document collections.

**Why Doc-Search-with-RAG?**

This project simplifies the creation of scalable, high-performance document search and summarization solutions. The core features include:

- 🧩 **🧠 Multi-format Document Ingestion:** Supports PDFs, Word, CSV, JSON, and more for versatile data integration.
- 🚀 **🔍 Semantic Search with FAISS:** Fast, accurate similarity search over high-dimensional vectors.
- 🎯 **🤖 Retrieval-Augmented Generation:** Combines document retrieval with language models for precise, context-aware answers.
- 🖥️ **✨ User-Friendly Interface:** Enables intuitive querying and summarization for end-users.
- ⚙️ **🔧 Modular & Configurable:** Easy to deploy, update, and customize within your architecture.

---

## 📌 Features

|      | Component       | Details                                                                                     |
| :--- | :-------------- | :------------------------------------------------------------------------------------------ |
| ⚙️  | **Architecture**  | <ul><li>Modular design separating data ingestion, embedding, retrieval, and UI</li><li>Uses LangChain for orchestration</li><li>Combines retrieval-augmented generation (RAG) with OpenAI models</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Clear project structure with dedicated folders for components</li><li>Uses `pyproject.toml` and `requirements.txt` for dependency management</li><li>Includes type hints and docstrings in key modules</li></ul> |
| 📄 | **Documentation** | <ul><li>README provides project overview, setup instructions, and usage examples</li><li>Code comments and docstrings present for functions/classes</li><li>Potential for further API documentation</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Leverages LangChain, OpenAI API, Sentence Transformers, ChromaDB, Typesense</li><li>Uses `langchain-openai`, `langchain`, `langchain-groq`, `langchain-community` packages</li><li>Supports PDF processing (`pypdf`, `mupdf`), vector stores, and search backends</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Components like data loaders, embedding models, and UI are decoupled</li><li>Configurable via environment variables and config files</li><li>Easy to swap models or storage backends</li></ul> |
| 🧪 | **Testing**       | <ul><li>Minimal explicit tests observed; potential for unit tests on core functions</li><li>Uses `uv.lock` and `requirements.txt` for environment consistency</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Utilizes FAISS (`faiss-cpu`) for fast vector similarity search</li><li>Embeddings generated via Sentence Transformers for efficiency</li><li>Streamlit UI for real-time interaction</li></ul> |
| 🛡️ | **Security**      | <ul><li>Uses environment variables (`python-dotenv`) for API keys</li><li>Potential for improved security practices in deployment</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Core dependencies include `langchain`, `faiss-cpu`, `pypdf`, `chromadb`, `sentence-transformers`, `streamlit`</li><li>Managed via `pyproject.toml` and `requirements.txt`</li></ul> |

---

## 🚀 Live Demo

👉 Click [here](doc-search-with-rag.streamlit.app) to check it out

---

## 📁 Project Structure

```sh
└── Doc-Search-with-RAG/
    ├── README.md
    ├── app.py
    ├── main.py
    ├── pyproject.toml
    ├── requirements.txt
    ├── src
    │   ├── __init__.py
    │   ├── config.py
    │   ├── data_loader.py
    │   ├── embedding.py
    │   ├── search.py
    │   └── vectorstore.py
    ├── ui.py
    └── uv.lock
```

---

### 📑 Project Index

<details open>
	<summary><b><code>DOC-SEARCH-WITH-RAG/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>- Defines the projects core configuration, specifying dependencies and metadata essential for building and running the application<br>- It ensures the environment includes necessary libraries for natural language processing, vector similarity search, PDF handling, and user interface components, facilitating seamless integration of data ingestion, retrieval, and interaction within the overall architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/README.md'>README.md</a></b></td>
					<td style='padding: 8px;'>- Provides essential guidance on redeploying the application within the overall architecture, ensuring smooth updates and maintenance<br>- Serves as a quick reference to facilitate efficient deployment processes, aligning with the projects goal of maintaining high availability and seamless updates across the system<br>- Supports operational stability by outlining best practices for redeployment procedures.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>- Provides the entry point for the rag-project, initiating the execution flow<br>- It serves as the starting script that outputs a greeting message, confirming the setup and readiness of the project environment<br>- This foundational component ensures the project can be launched and tested easily, acting as a simple verification of the overall systems operational status.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/app.py'>app.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates document ingestion, vector store creation, and retrieval-augmented generation (RAG) search within the application architecture<br>- It orchestrates data loading, index building, and querying processes to enable efficient semantic search and summarization capabilities, serving as the core entry point for leveraging stored knowledge and generating concise responses based on relevant document retrievals.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/ui.py'>ui.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates user interaction with the document retrieval system by providing a streamlined interface for querying and receiving summarized answers<br>- Integrates the RAG-based search component to enable efficient question-answering over document embeddings, supporting an intuitive experience for exploring and extracting insights from the underlying knowledge base within the overall architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Defines project dependencies essential for building a comprehensive AI-powered knowledge management platform<br>- Integrates language processing, document handling, vector similarity search, and user interface components to enable seamless document ingestion, semantic search, and interactive data exploration within the broader architecture<br>- Supports scalable, modular development of intelligent applications leveraging advanced NLP and data retrieval techniques.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- src Submodule -->
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ src</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/src/data_loader.py'>data_loader.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates comprehensive ingestion of various document formats from a specified directory, converting them into a unified structure suitable for downstream processing<br>- Supports PDF, TXT, CSV, Excel, Word, and JSON files, enabling seamless integration of diverse data sources for tasks such as analysis, indexing, or machine learning workflows within the broader system architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/src/embedding.py'>embedding.py</a></b></td>
					<td style='padding: 8px;'>- Provides an embedding pipeline that processes textual documents by splitting them into manageable chunks and generating vector representations using a sentence transformer model<br>- Facilitates efficient semantic understanding and retrieval within the larger architecture, enabling downstream tasks such as search, similarity comparison, or knowledge integration across the project’s document corpus.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/src/search.py'>search.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates retrieval-augmented question answering by integrating a vector store with language models to fetch relevant documents and generate precise, reference-based summaries<br>- It orchestrates document embedding, storage, and querying, enabling efficient, context-aware responses that adhere strictly to provided data, thereby supporting knowledge extraction and summarization within the overall system architecture.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/src/vectorstore.py'>vectorstore.py</a></b></td>
					<td style='padding: 8px;'>- Implements a vector store leveraging FAISS for efficient similarity search over document embeddings<br>- Facilitates building, saving, loading, and querying high-dimensional vectors derived from textual data, enabling rapid retrieval of relevant information based on semantic similarity within the overall architecture<br>- This component is essential for enabling scalable, accurate retrieval in applications like question-answering or information retrieval systems.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/surya-adina/Doc-Search-with-RAG/blob/master/src/config.py'>config.py</a></b></td>
					<td style='padding: 8px;'>- Defines the data directory path used across the project, enabling flexible configuration through environment variables<br>- Facilitates centralized management of data storage location, supporting adaptable deployment environments and ensuring consistent access to datasets essential for the applications core functionalities<br>- This configuration underpins data handling within the overall architecture, promoting modularity and ease of customization.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 📋 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Uv, Pip

### ⚙️ Installation

Build Doc-Search-with-RAG from the source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/surya-adina/Doc-Search-with-RAG
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Doc-Search-with-RAG
    ```

3. **Install the dependencies:**

**Using [uv](https://docs.astral.sh/uv/):**

```sh
❯ uv sync --all-extras --dev
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
❯ pip install -r requirements.txt
```

### 💻 Usage

Run the project with:

**Using [uv](https://docs.astral.sh/uv/):**

```sh
uv run python {entrypoint}
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
python {entrypoint}
```

### 🧪 Testing

Doc-search-with-rag uses the {__test_framework__} test framework. Run the test suite with:

**Using [uv](https://docs.astral.sh/uv/):**

```sh
uv run pytest tests/
```
**Using [pip](https://pypi.org/project/pip/):**

```sh
pytest
```


---

<div align="left"><a href="#top">⬆ Return</a></div>

---
