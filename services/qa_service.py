from core.prompt_builder import PromptBuilder
from memory.memory_manager import MemoryManager


class QAService:

    def __init__(
        self,
        retriever,
        llm,
    ):

        self.retriever = retriever
        self.llm = llm

        self.builder = PromptBuilder()

        self.memory = MemoryManager()

    def ask(
        self,
        question: str,
    ):

        # Store user message
        self.memory.add_user(
            question
        )

        # Retrieve relevant chunks
        results = self.retriever.hybrid_retrieve(
            question
        )

        if not results:

            answer = "No relevant information found."

            self.memory.add_assistant(
                answer
            )

            return {
                "answer": answer,
                "sources": [],
            }

        # Build prompt with conversation history
        prompt = self.builder.build(
            question=question,
            results=results,
            conversation=self.memory.get_context(),
        )

        # Generate answer
        answer = self.llm.generate(
            prompt
        )

        # Store assistant answer
        self.memory.add_assistant(
            answer
        )

        return {

            "answer": answer,

            "sources": results,

        }