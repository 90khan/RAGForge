from providers.ollama_provider import OllamaProvider


class LLM:

    def __init__(self):

        self.provider = OllamaProvider()

    def generate(
        self,
        prompt: str,
        max_tokens: int = 512,
    ):

        return self.provider.generate(
            prompt,
            max_tokens,
        )
