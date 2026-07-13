from sentence_transformers import CrossEncoder

from models.search import SearchResult


class CrossEncoderReranker:

    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    ):

        self.model = CrossEncoder(
            model_name,
        )

    def rerank(
        self,
        query: str,
        results: list[SearchResult],
        top_k: int = 5,
    ) -> list[SearchResult]:

        if not results:
            return []

        pairs = [(query, result.chunk.text) for result in results]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(scores, results),
            key=lambda x: x[0],
            reverse=True,
        )

        return [result for _, result in ranked[:top_k]]
