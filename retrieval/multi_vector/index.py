from retrieval.multi_vector.document_encoder import (
    MultiVectorEncoder,
)

from vectorstore.multi_vector_store import (
    MultiVectorStore,
)


class MultiVectorIndex:

    def __init__(
        self,
        embedding_provider,
    ):

        self.embedding = embedding_provider

        self.encoder = MultiVectorEncoder()

    def build(
        self,
        chunks,
    ):

        first_vectors = self.encoder.encode(
            chunks[0]
        )

        dimension = self.embedding.embed_documents(
            first_vectors
        ).shape[1]

        store = MultiVectorStore(
            dimension
        )

        for chunk in chunks:

            texts = self.encoder.encode(
                chunk
            )

            vectors = self.embedding.embed_documents(
                texts
            )

            store.add(
                chunk,
                vectors,
            )

        return store