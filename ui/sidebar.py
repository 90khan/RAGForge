import streamlit as st


class Sidebar:

    def render(self):

        st.sidebar.title("⚙ Settings")

        top_k = st.sidebar.slider(
            "Top K",
            1,
            10,
            5,
        )

        threshold = st.sidebar.slider(
            "Similarity",
            0.0,
            1.0,
            0.55,
        )

        return {
            "top_k": top_k,
            "threshold": threshold,
        }
