from collections import defaultdict

from models.search import SearchResult


class ReciprocalRankFusion:
    """
    Reciprocal Rank Fusion (RRF)

    Supports any number of ranked lists.
    """

    def __init__(
        self,
        k: int = 60,
    ):

        self.k = k

    def fuse(
        self,
        *rankings: list[SearchResult],
    ) -> list[SearchResult]:

        scores = defaultdict(float)

        results = {}

        for ranking in rankings:

            if not ranking:
                continue

            for rank, result in enumerate(
                ranking,
                start=1,
            ):

                chunk_id = result.chunk.id

                scores[
                    chunk_id
                ] += 1 / (
                    self.k + rank
                )

                if chunk_id not in results:

                    results[
                        chunk_id
                    ] = result

        ranked = sorted(

            scores.items(),

            key=lambda item: item[1],

            reverse=True,

        )

        return [

            results[chunk_id]

            for chunk_id, _ in ranked

        ]