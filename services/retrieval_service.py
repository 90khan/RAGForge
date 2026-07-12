from typing import List

from models.search import SearchResult


class RetrievalService:

    def __init__(
        self,
        store,
        embedding_provider,
    ):

        self.store = store
        self.embedding = embedding_provider

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.55,
    ) -> List[SearchResult]:

        query_vector = self.embedding.embed_query(
            query
        )

        results = self.store.search(
            query_vector,
            top_k,
        )

        return [

            result

            for result in results

            if result.score >= min_score

        ]