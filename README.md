# 🔥 RAGForge

> A production-ready Retrieval-Augmented Generation (RAG) framework built with pure Python.

RAGForge is a modular and extensible RAG framework designed for building intelligent document question-answering systems. It combines dense retrieval, lexical retrieval, graph-based retrieval, reranking, citations, and modern LLM techniques into a clean architecture suitable for production environments.

---

# ✨ Features

- 📄 PDF & DOCX document ingestion
- ✂️ Intelligent document chunking
- 🔍 FAISS vector search
- 🔎 BM25 lexical search
- 🔀 Hybrid Retrieval
- 🏆 Reciprocal Rank Fusion (RRF)
- 🎯 CrossEncoder reranking
- 🕸️ GraphRAG
- 🧠 Multi-Vector Retrieval
- 💡 HyDE Query Expansion
- 📚 Citation Engine
- 💬 Conversation Memory
- 🤖 Ollama LLM integration
- ⚡ FastAPI REST API
- 🎨 Streamlit Web UI
- 🐳 Docker support
- ✅ Pytest unit tests

---

# 🏗️ Architecture

```
                   Documents
               (PDF / DOCX)
                      │
                      ▼
               Loader Factory
                      │
                      ▼
                  Chunker
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
   FAISS            BM25          GraphRAG
      │               │                │
      └───────────────┼────────────────┘
                      ▼
          Reciprocal Rank Fusion
                      ▼
          CrossEncoder Reranker
                      ▼
            Citation Builder
                      ▼
              Prompt Builder
                      ▼
                 Ollama LLM
                      ▼
                 Final Answer
```

---

# 📂 Project Structure

```
RAGForge/
│
├── api/
├── citation/
├── core/
├── data/
├── demos/
├── evaluation/
├── graph/
├── loaders/
├── memory/
├── models/
├── providers/
├── reranking/
├── retrieval/
├── services/
├── tests/
├── ui/
├── vectorstore/
│
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/RAGForge.git

cd RAGForge
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Streamlit

```bash
streamlit run app.py
```

---

# ⚡ Running FastAPI

```bash
uvicorn api.server:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker compose -f docker/docker-compose.yml build
```

Run

```bash
docker compose -f docker/docker-compose.yml up
```

---

# 🔍 REST API

## Index Document

```
POST /index
```

Upload a PDF or DOCX document for indexing.

---

## Retrieve

```
POST /retrieve
```

Example

```json
{
    "question": "What is RAG?",
    "top_k": 5
}
```

---

## Chat

```
POST /chat
```

Example

```json
{
    "question": "Explain GraphRAG."
}
```

---

# 🧪 Testing

Run all unit tests

```bash
pytest
```

Current Status

```
5 passed
```

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| UI | Streamlit |
| API | FastAPI |
| Vector Search | FAISS |
| Lexical Search | BM25 |
| Graph | NetworkX |
| Embeddings | SentenceTransformers |
| Reranking | CrossEncoder |
| LLM | Ollama |
| Testing | Pytest |
| Container | Docker |

---

# 📈 Roadmap

- [x] FAISS Retrieval
- [x] BM25 Retrieval
- [x] Hybrid Search
- [x] GraphRAG
- [x] Multi-Vector Retrieval
- [x] HyDE
- [x] RRF
- [x] CrossEncoder
- [x] Citation Engine
- [x] FastAPI
- [x] Streamlit
- [x] Docker
- [x] Unit Tests
- [ ] Benchmark Dashboard
- [ ] Multi-user Authentication
- [ ] Cloud Deployment
- [ ] Kubernetes Support

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Gökhan Usluer**

Senior AI Engineer

- Python
- GenAI
- LLM
- RAG
- GraphRAG
- MLOps
- FastAPI