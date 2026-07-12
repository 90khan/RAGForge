from providers.embedding_factory import (
    EmbeddingFactory,
)

from vectorstore.faiss_store import (
    FAISSStore,
)


class VectorService:

    def __init__(self):

        self.embedding = (
            EmbeddingFactory.create()
        )

        self.store = None

    def build(
        self,
        document,
    ):

        texts = [
            chunk.text
            for chunk in document.chunks
        ]

        vectors = self.embedding.embed(
            texts
        )

        self.store = FAISSStore(
            vectors.shape[1]
        )

        self.store.add(
            document.chunks,
            vectors,
        )

        return self.store