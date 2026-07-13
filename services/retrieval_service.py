from typing import List

from models.search import SearchResult

from retrieval.query_processor import QueryProcessor
from retrieval.query_expander import QueryExpander
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

        self.processor = QueryProcessor()
        self.expander = QueryExpander()

        self.rrf = ReciprocalRankFusion()
        self.reranker = CrossEncoderReranker()

    def retrieve(
        self,
        processed_query: str,
        top_k: int = 5,
        min_score: float = 0.55,
    ) -> List[SearchResult]:

        query_vector = self.embedding.embed_query(
            processed_query
        )

        return self.search_vector(
            query_vector=query_vector,
            query=processed_query,
            top_k=top_k,
            min_score=min_score,
        )

    def hybrid_retrieve(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.55,
    ) -> List[SearchResult]:

        query = self.processor.process(
            query
        )

        query = self.expander.expand(
            query
        )

        return self.retrieve(
            processed_query=query,
            top_k=top_k,
            min_score=min_score,
        )

    def search_vector(
        self,
        query_vector,
        query: str,
        top_k: int = 5,
        min_score: float = 0.55,
    ) -> List[SearchResult]:

        semantic = self.store.search(
            query_vector,
            max(top_k * 2, 10),
        )

        semantic = [
            result
            for result in semantic
            if result.score >= min_score
        ]

        if self.bm25 is None:

            return self.reranker.rerank(
                query=query,
                results=semantic,
                top_k=top_k,
            )

        lexical = self.bm25.search(
            query=query,
            top_k=max(top_k * 2, 10),
        )

        fused = self.rrf.fuse(
            semantic=semantic,
            lexical=lexical,
        )

        return self.reranker.rerank(
            query=query,
            results=fused,
            top_k=top_k,
        )