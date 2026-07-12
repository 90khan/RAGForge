from typing import List

from models.search import SearchResult


class RetrievalService:

    def __init__(
        self,
        store,
        embedding_provider,
        bm25=None,
    ):
        self.store = store
        self.embedding = embedding_provider
        self.bm25 = bm25

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.55,
    ) -> List[SearchResult]:

        query_vector = self.embedding.embed_query(query)

        results = self.store.search(
            query_vector,
            top_k,
        )

        return [
            result
            for result in results
            if result.score >= min_score
        ]

    def hybrid_retrieve(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.55,
    ) -> List[SearchResult]:

        query_vector = self.embedding.embed_query(query)

        semantic = self.store.search(
            query_vector,
            top_k,
        )

        semantic = [
            r
            for r in semantic
            if r.score >= min_score
        ]

        if self.bm25 is None:
            return semantic

        lexical = self.bm25.search(
            query,
            top_k,
        )

        merged = []
        seen = set()

        for result in semantic:
            merged.append(result)
            seen.add(result.chunk.id)

        for score, chunk in lexical:

            if chunk.id in seen:
                continue

            merged.append(
                SearchResult(
                    chunk=chunk,
                    score=float(score),
                    source=chunk.metadata["source"],
                    page=chunk.metadata.get("page"),
                )
            )

        merged.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return merged[:top_k]