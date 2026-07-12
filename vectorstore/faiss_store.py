import faiss
import numpy as np


class FAISSStore:

    def __init__(self, dimension: int):

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.documents = []

    def add(self, embeddings, texts):

        embeddings = np.asarray(
            embeddings,
            dtype="float32",
        )

        self.index.add(
            embeddings
        )

        self.documents.extend(texts)

    def search(
        self,
        embedding,
        top_k=3,
    ):

        embedding = np.asarray(
            [embedding],
            dtype="float32",
        )

        scores, indices = self.index.search(
            embedding,
            top_k,
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0],
        ):

            if idx == -1:
                continue

            results.append(
                {
                    "score": float(score),
                    "text": self.documents[idx],
                }
            )

        return results