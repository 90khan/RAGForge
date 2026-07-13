from models.search import SearchResult


class PromptBuilder:

    SYSTEM_PROMPT = """
You are an AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found,
reply exactly:

I couldn't find this information in the provided documents.
"""

    def build(
        self,
        question: str,
        results: list[SearchResult],
        conversation: str = "",
    ) -> str:

        context = []

        for result in results:

            context.append(
                f"""
Source: {result.source.name}

Page: {result.page}

Content:

{result.chunk.text}
"""
            )

        context_text = "\n".join(context)

        return f"""
{self.SYSTEM_PROMPT}

Conversation

{conversation}

Context

{context_text}

Question

{question}

Answer
"""
