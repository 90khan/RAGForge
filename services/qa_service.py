from core.prompt_builder import PromptBuilder

from memory.memory_manager import (
    MemoryManager,
)


class QAService:

    def __init__(
        self,
        retriever,
        llm,
    ):

        self.retriever = retriever

        self.llm = llm

        self.prompt_builder = (
            PromptBuilder()
        )

        self.memory = (
            MemoryManager()
        )

    def ask(
        self,
        question: str,
    ):

        # -------------------------
        # Conversation Memory
        # -------------------------

        self.memory.add_user(
            question
        )

        # -------------------------
        # Retrieval
        # -------------------------

        results = self.retriever.hybrid_retrieve(
            question
        )

        if not results:

            answer = (
                "No relevant information found."
            )

            self.memory.add_assistant(
                answer
            )

            return {

                "answer": answer,

                "sources": [],

            }

        # -------------------------
        # Prompt
        # -------------------------

        prompt = self.prompt_builder.build(

            question=question,

            results=results,

            conversation=self.memory.get_context(),

        )

        # -------------------------
        # LLM
        # -------------------------

        answer = self.llm.generate(
            prompt
        )

        # -------------------------
        # Update Memory
        # -------------------------

        self.memory.add_assistant(
            answer
        )

        return {

            "answer": answer,

            "sources": results,

        }