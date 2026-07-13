from providers.sentence_transformer_provider import (
    SentenceTransformerProvider,
)


class EmbeddingFactory:

    @staticmethod
    def create():

        return SentenceTransformerProvider()
