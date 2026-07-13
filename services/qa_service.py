from core.prompt_builder import PromptBuilder


class QAService:

    def __init__(
        self,
        retriever,
        llm,
    ):

        self.retriever = retriever
        self.llm = llm

        self.builder = PromptBuilder()

    def ask(
        self,
        question: str,
    ):

        results = self.retriever.hybrid_retrieve(
            question
        )

        if not results:

            return {
                "answer": "No relevant information found.",
                "sources": [],
            }

        prompt = self.builder.build(
            question,
            results,
        )

        answer = self.llm.generate(
            prompt
        )

        return {

            "answer": answer,

            "sources": results,

        }