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
        question,
    ):

        results = self.retriever.hybrid_retrieve(
                                        question
        )

        if not results:

            return "No relevant information found."

        prompt = self.builder.build(
            question,
            results,
        )

        return self.llm.generate(
            prompt
        )