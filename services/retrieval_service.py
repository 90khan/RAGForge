from typing import List

from models.search import SearchResult
from retrieval.rrf import ReciprocalRankFusion
from reranking.cross_encoder import CrossEncoderReranker


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

        self.rrf = ReciprocalRankFusion()
        self.reranker = CrossEncoderReranker()

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

        # Semantic Search
        semantic = self.retrieve(
            query=query,
            top_k=max(top_k * 2, 10),
            min_score=min_score,
        )

        # Eğer BM25 yoksa sadece rerank yap
        if self.bm25 is None:
            return self.reranker.rerank(
                query=query,
                results=semantic,
                top_k=top_k,
            )

        # BM25 Search
        lexical = self.bm25.search(
            query=query,
            top_k=max(top_k * 2, 10),
        )

        # RRF Fusion
        fused = self.rrf.fuse(
            semantic=semantic,
            lexical=lexical,
        )

        # CrossEncoder Reranking
        reranked = self.reranker.rerank(
            query=query,
            results=fused,
            top_k=top_k,
        )

        return reranked