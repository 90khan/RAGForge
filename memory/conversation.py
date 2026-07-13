from dataclasses import dataclass, field


@dataclass(slots=True)
class Message:

    role: str
    content: str


@dataclass(slots=True)
class Conversation:

    messages: list[Message] = field(
        default_factory=list
    )

    def add_user(
        self,
        content: str,
    ):

        self.messages.append(

            Message(

                role="user",

                content=content,

            )

        )

    def add_assistant(
        self,
        content: str,
    ):

        self.messages.append(

            Message(

                role="assistant",

                content=content,

            )

        )

    def last(
        self,
        n: int = 6,
    ) -> list[Message]:

        return self.messages[-n:]

    def clear(self):

        self.messages.clear()