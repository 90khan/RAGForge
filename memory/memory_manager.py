from memory.conversation import Conversation


class MemoryManager:

    def __init__(self):

        self.conversation = Conversation()

    def add_user(
        self,
        question: str,
    ):

        self.conversation.add_user(question)

    def add_assistant(
        self,
        answer: str,
    ):

        self.conversation.add_assistant(answer)

    def get_context(
        self,
        limit: int = 6,
    ) -> str:

        history = []

        for message in self.conversation.last(limit):

            history.append(f"{message.role}: {message.content}")

        return "\n".join(history)

    def clear(self):

        self.conversation.clear()
