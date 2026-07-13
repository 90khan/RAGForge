from pathlib import Path

import streamlit as st


UPLOAD_DIR = Path("data/uploads")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


class UploadUI:

    def render(self):

        uploaded = st.sidebar.file_uploader(

            "Upload PDF",

            type=["pdf"],

        )

        if uploaded is None:
            return None

        destination = UPLOAD_DIR / uploaded.name

        with open(destination, "wb") as f:

            f.write(uploaded.getbuffer())

        st.sidebar.success("PDF uploaded.")

        return destination