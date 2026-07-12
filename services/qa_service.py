from core.prompts import SYSTEM_PROMPT


class QAService:

    def __init__(

        self,

        retriever,

        llm,

    ):

        self.retriever = retriever

        self.llm = llm

    def ask(

        self,

        question: str,

    ):

        results = self.retriever.retrieve(
            question
        )

        context = "\n\n".join(

            r.chunk.text

            for r in results

        )

        prompt = SYSTEM_PROMPT.format(

            context=context,

            question=question,

        )

        return self.llm.generate(
            prompt
        )