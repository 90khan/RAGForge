from config.settings import LLM_PROVIDER

from providers.huggingface_provider import HuggingFaceProvider
from providers.ollama_provider import OllamaProvider


class LLMFactory:

    @staticmethod
    def create():

        provider = LLM_PROVIDER.lower()

        if provider == "ollama":
            return OllamaProvider()

        if provider == "huggingface":
            return HuggingFaceProvider()

        raise ValueError(f"Unknown provider: {provider}")