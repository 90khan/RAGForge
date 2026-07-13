from collections import defaultdict

from retrieval.multi_vector.document_encoder import (
    MultiVectorEncoder,
)


class MultiVectorIndex:

    """
    Creates multiple embeddings
    for every chunk.

    One chunk
        ↓
    Original
    Summary
    Source
        ↓
    Embeddings
    """

    def __init__(
        self,
        embedding_provider,
    ):

        self.embedding = embedding_provider

        self.encoder = MultiVectorEncoder()

        self.index = defaultdict(list)

    def build(
        self,
        chunks,
    ):

        self.index.clear()

        for chunk in chunks:

            texts = self.encoder.encode(
                chunk
            )

            vectors = self.embedding.embed_documents(
                texts
            )

            for vector in vectors:

                self.index[
                    chunk.id
                ].append(vector)

        return self.index