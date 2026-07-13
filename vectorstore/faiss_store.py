import faiss
import numpy as np

from models.document import Chunk
from models.search import SearchResult

from vectorstore.base_store import BaseVectorStore


class FAISSStore(BaseVectorStore):

    def __init__(self, dimension: int):

        self.index = faiss.IndexFlatIP(dimension)

        self.chunks: list[Chunk] = []

    def add(
        self,
        chunks,
        embeddings,
    ):

        embeddings = np.asarray(
            embeddings,
            dtype=np.float32,
        )

        self.index.add(embeddings)

        self.chunks.extend(chunks)

    def search(
        self,
        embedding,
        top_k=5,
    ):

        embedding = np.asarray(
            [embedding],
            dtype=np.float32,
        )

        scores, ids = self.index.search(
            embedding,
            top_k,
        )

        results = []

        for score, idx in zip(
            scores[0],
            ids[0],
        ):

            if idx == -1:
                continue

            results.append(
                SearchResult(
                    chunk=self.chunks[idx],
                    score=float(score),
                    source=self.chunks[idx].metadata["source"],
                    page=self.chunks[idx].metadata.get("page"),
                )
            )

        return results
