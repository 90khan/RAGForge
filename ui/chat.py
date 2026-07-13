import streamlit as st

from citation.formatter import CitationFormatter


class ChatUI:

    def __init__(self):

        if "messages" not in st.session_state:

            st.session_state.messages = []

        self.formatter = CitationFormatter()

    def render_history(self):

        for message in st.session_state.messages:

            with st.chat_message(
                message["role"]
            ):

                st.markdown(
                    message["content"]
                )

    def add_user_message(
        self,
        message: str,
    ):

        st.session_state.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(
        self,
        message: str,
    ):

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    # ---------------------------------
    # Legacy Sources
    # ---------------------------------

    def show_sources(
        self,
        sources,
    ):

        if not sources:
            return

        with st.expander(
            "📚 Sources"
        ):

            shown = set()

            for result in sources:

                key = (
                    result.source,
                    result.page,
                )

                if key in shown:
                    continue

                shown.add(
                    key
                )

                st.markdown(
                    f"""
**📄 {result.source.name}**

Page: {result.page}

Score: {result.score:.3f}
"""
                )

    # ---------------------------------
    # Citation Engine
    # ---------------------------------

    def show_citations(
        self,
        citations,
    ):

        if not citations:

            return

        with st.expander(
            "📚 Citations"
        ):

            st.markdown(

                self.formatter.markdown(
                    citations
                )

            )