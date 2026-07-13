from typing import List

from graph.graph_retriever import GraphRetriever

from models.search import SearchResult

from retrieval.query_expander import QueryExpander
from retrieval.query_processor import QueryProcessor
from retrieval.rrf import ReciprocalRankFusion

from reranking.cross_encoder import CrossEncoderReranker


class RetrievalService:

    def __init__(
        self,
        store,
        embedding_provider,
        bm25=None,
        graph_store=None,
    ):

        self.store = store
        self.embedding = embedding_provider

        self.bm25 = bm25

        self.processor = QueryProcessor()
        self.expander = QueryExpander()

        self.rrf = ReciprocalRankFusion()

        self.reranker = CrossEncoderReranker()

        self.graph = None

        if graph_store is not None:

            self.graph = GraphRetriever(
                graph_store
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

        query_vector = self.embedding.embed_query(
            query
        )

        return self.search(
            query=query,
            query_vector=query_vector,
            top_k=top_k,
            min_score=min_score,
        )

    def search(
        self,
        query: str,
        query_vector,
        top_k: int,
        min_score: float,
    ) -> List[SearchResult]:

        # ---------------------------------
        # Semantic Search
        # ---------------------------------

        semantic = self.store.search(
            query_vector,
            max(top_k * 2, 10),
        )

        semantic = [
            result
            for result in semantic
            if result.score >= min_score
        ]

        # ---------------------------------
        # BM25
        # ---------------------------------

        lexical = []

        if self.bm25 is not None:

            lexical = self.bm25.search(
                query=query,
                top_k=max(top_k * 2, 10),
            )

        # ---------------------------------
        # Graph Retrieval
        # ---------------------------------

        graph_results = []

        if self.graph is not None:

            chunks = self.graph.retrieve(
                query
            )

            graph_results = [

                SearchResult(
                    chunk=chunk,
                    score=1.0,
                    source=chunk.metadata["source"],
                    page=chunk.metadata.get("page"),
                )

                for chunk in chunks

            ]

        # ---------------------------------
        # Reciprocal Rank Fusion
        # ---------------------------------

        fused = self.rrf.fuse(
            semantic,
            lexical,
            graph_results,
        )

        # ---------------------------------
        # CrossEncoder Reranking
        # ---------------------------------

        return self.reranker.rerank(
            query=query,
            results=fused,
            top_k=top_k,
        )