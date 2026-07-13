import faiss
import numpy as np

from models.search import SearchResult


class MultiVectorStore:
    """
    FAISS index that stores multiple vectors
    for the same chunk.
    """

    def __init__(
        self,
        dimension: int,
    ):

        self.index = faiss.IndexFlatIP(dimension)

        self.vector_to_chunk = []

        self.chunks = {}

    def add(
        self,
        chunk,
        embeddings,
    ):

        embeddings = np.asarray(
            embeddings,
            dtype=np.float32,
        )

        self.index.add(embeddings)

        self.chunks[chunk.id] = chunk

        self.vector_to_chunk.extend([chunk.id] * len(embeddings))

    def search(
        self,
        embedding,
        top_k=10,
    ):

        embedding = np.asarray(
            [embedding],
            dtype=np.float32,
        )

        scores, ids = self.index.search(
            embedding,
            top_k,
        )

        merged = {}

        for score, vector_id in zip(
            scores[0],
            ids[0],
        ):

            if vector_id == -1:
                continue

            chunk_id = self.vector_to_chunk[vector_id]

            if chunk_id not in merged or score > merged[chunk_id]:

                merged[chunk_id] = float(score)

        results = []

        for chunk_id, score in merged.items():

            chunk = self.chunks[chunk_id]

            results.append(
                SearchResult(
                    chunk=chunk,
                    score=score,
                    source=chunk.metadata["source"],
                    page=chunk.metadata.get("page"),
                )
            )

        results.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return results
