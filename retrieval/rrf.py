from collections import defaultdict

from models.search import SearchResult


class ReciprocalRankFusion:
    """
    Reciprocal Rank Fusion (RRF)

    Paper:
    Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods.
    """

    def __init__(self, k: int = 60):
        self.k = k

    def fuse(
        self,
        semantic: list[SearchResult],
        lexical: list[SearchResult],
    ) -> list[SearchResult]:

        scores = defaultdict(float)
        results = {}

        # Semantic ranking
        for rank, result in enumerate(semantic, start=1):
            scores[result.chunk.id] += 1 / (self.k + rank)
            results[result.chunk.id] = result

        # BM25 ranking
        for rank, result in enumerate(lexical, start=1):

            scores[result.chunk.id] += 1 / (self.k + rank)

            if result.chunk.id not in results:
                results[result.chunk.id] = result

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            results[chunk_id]
            for chunk_id, _ in ranked
        ]