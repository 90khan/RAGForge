class HyDEGenerator:
    """
    Generates a hypothetical document
    from the user query.
    """

    def __init__(
        self,
        llm,
    ):

        self.llm = llm

    def generate(
        self,
        query: str,
    ) -> str:

        prompt = f"""
You are an expert technical writer.

Write a concise document that correctly answers
the following question.

Question:

{query}

Document:
"""

        return self.llm.generate(prompt)
