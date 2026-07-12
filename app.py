import streamlit as st

from core.llm import LLMFactory

st.set_page_config(
    page_title="RAGForge",
    layout="wide"
)

st.title("🔥 RAGForge")

llm = LLMFactory.create()

question = st.text_input(
    "Ask something"
)

if st.button("Generate"):

    if question:

        with st.spinner("Thinking..."):

            answer = llm.generate(question)

        st.success(answer)