import numpy as np


class MultiVectorRetriever:

    """
    Searches over multiple vectors
    belonging to the same chunk.

    Final score
        =
    Maximum similarity
    """

    def __init__(
        self,
        store,
        multi_index,
    ):

        self.store = store

        self.index = multi_index

    def search(
        self,
        query_vector,
        top_k=5,
    ):

        scores = []

        for chunk_id, vectors in self.index.items():

            best = -1.0

            for vector in vectors:

                similarity = float(

                    np.dot(
                        query_vector,
                        vector,
                    )

                )

                if similarity > best:

                    best = similarity

            scores.append(

                (

                    chunk_id,

                    best,

                )

            )

        scores.sort(

            key=lambda x: x[1],

            reverse=True,

        )

        return scores[:top_k]