from pathlib import Path

import streamlit as st

from core.chunker import TextChunker
from core.llm import LLM

from loaders.loader_factory import LoaderFactory

from services.index_service import IndexService
from services.qa_service import QAService
from services.retrieval_service import RetrievalService

from ui.chat import ChatUI
from ui.sidebar import Sidebar
from ui.upload import UploadUI


st.set_page_config(
    page_title="RAGForge",
    page_icon="🔥",
    layout="wide",
)

st.title("🔥 RAGForge")
st.caption(
    "Pure Python • FAISS • BM25 • RRF • CrossEncoder"
)


# ----------------------------
# Sidebar
# ----------------------------

sidebar = Sidebar()
settings = sidebar.render()


# ----------------------------
# Upload
# ----------------------------

upload = UploadUI()

uploaded_file = upload.render()

if uploaded_file is None:

    uploaded_file = Path(
        "data/uploads/example.pdf"
    )


# ----------------------------
# Build Pipeline
# ----------------------------

@st.cache_resource(show_spinner=False)
def build_pipeline(file_path: Path):

    loader = LoaderFactory.create(
        file_path
    )

    document = loader.load(
        file_path
    )

    chunker = TextChunker()

    document = chunker.split(
        document
    )

    index = IndexService()

    store = index.build_index(
        document
    )

    retriever = RetrievalService(
        store=store,
        embedding_provider=index.embedding_provider,
        bm25=index.bm25,
    )

    llm = LLM()

    return QAService(
        retriever=retriever,
        llm=llm,
    )


qa = build_pipeline(
    uploaded_file
)

chat = ChatUI()


# ----------------------------
# Chat History
# ----------------------------

chat.render_history()


# ----------------------------
# Chat Input
# ----------------------------

question = st.chat_input(
    "Ask your question..."
)

if question:

    chat.add_user_message(
        question
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = qa.ask(
                question
            )

            st.markdown(
                response["answer"]
            )

    chat.add_assistant_message(
        response["answer"]
    )

    chat.show_sources(
        response["sources"]
    )