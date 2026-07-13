from models.search import SearchResult


class RetrievalMetrics:

    @staticmethod
    def recall_at_k(
        results: list[SearchResult],
        relevant_ids: list[str],
    ) -> float:

        if not relevant_ids:

            return 0.0

        retrieved = {result.chunk.id for result in results}

        hits = len(retrieved & set(relevant_ids))

        return hits / len(relevant_ids)

    @staticmethod
    def precision_at_k(
        results: list[SearchResult],
        relevant_ids: list[str],
    ) -> float:

        if not results:

            return 0.0

        hits = sum(1 for result in results if result.chunk.id in relevant_ids)

        return hits / len(results)

    @staticmethod
    def hit_rate(
        results: list[SearchResult],
        relevant_ids: list[str],
    ) -> float:

        for result in results:

            if result.chunk.id in relevant_ids:

                return 1.0

        return 0.0

    @staticmethod
    def mrr(
        results: list[SearchResult],
        relevant_ids: list[str],
    ) -> float:

        for rank, result in enumerate(
            results,
            start=1,
        ):

            if result.chunk.id in relevant_ids:

                return 1 / rank

        return 0.0
