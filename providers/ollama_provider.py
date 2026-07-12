import ollama

from config.settings import OLLAMA_MODEL
from .base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(self):

        self.model = OLLAMA_MODEL

    def health_check(self):

        try:

            ollama.list()

            return True

        except Exception:

            return False

    def generate(
        self,
        prompt,
        max_new_tokens=256,
    ):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options={
                "num_predict": max_new_tokens,
            },
        )

        return response["message"]["content"]