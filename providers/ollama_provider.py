import ollama

from config.settings import settings

from providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(self):

        self.model = settings.ollama_model

    def generate(
        self,
        prompt: str,
        max_tokens: int = 512,
    ) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options={
                "num_predict": max_tokens,
                "temperature": 0,
            },
        )

        return response.message.content
