from models.document import Document

from providers.embedding_factory import (
    EmbeddingFactory,
)


class EmbeddingService:

    def __init__(self):

        self.provider = (
            EmbeddingFactory.create()
        )

    def embed(
        self,
        document: Document,
    ) -> Document:

        texts = [
            chunk.text
            for chunk in document.chunks
        ]

        vectors = self.provider.embed(
            texts
        )

        for chunk, vector in zip(
            document.chunks,
            vectors,
        ):

            chunk.embedding = vector

        return document