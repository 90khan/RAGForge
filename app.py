from pathlib import Path

import streamlit as st

from services.pipeline_service import PipelineService

from ui.chat import ChatUI
from ui.sidebar import Sidebar
from ui.upload import UploadUI


# --------------------------------------------------
# Page
# --------------------------------------------------

st.set_page_config(
    page_title="RAGForge",
    page_icon="🔥",
    layout="wide",
)

st.title("🔥 RAGForge")
st.caption(
    "Pure Python • FAISS • BM25 • RRF • CrossEncoder • GraphRAG"
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

sidebar = Sidebar()

settings = sidebar.render()


# --------------------------------------------------
# Upload
# --------------------------------------------------

upload = UploadUI()

uploaded_file = upload.render()

if uploaded_file is None:

    uploaded_file = Path(
        "data/uploads/example.pdf"
    )


# --------------------------------------------------
# Build QA Pipeline
# --------------------------------------------------

@st.cache_resource(show_spinner=False)
def build_pipeline(
    file_path: Path,
):

    return PipelineService().build(
        file_path
    )


qa = build_pipeline(
    uploaded_file
)


# --------------------------------------------------
# Chat UI
# --------------------------------------------------

chat = ChatUI()

chat.render_history()


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask your question..."
)


# --------------------------------------------------
# Chat
# --------------------------------------------------

if question:

    chat.add_user_message(
        question
    )

    with st.chat_message("user"):

        st.markdown(
            question
        )

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