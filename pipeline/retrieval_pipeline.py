from retrieval.query_processor import QueryProcessor
from retrieval.query_expander import QueryExpander


class RetrievalPipeline:

    def __init__(
        self,
        retrieval_service,
        hyde_service=None,
    ):

        self.processor = QueryProcessor()

        self.expander = QueryExpander()

        self.retrieval = retrieval_service

        self.hyde = hyde_service

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        query = self.processor.process(
            query
        )

        query = self.expander.expand(
            query
        )

        if self.hyde:

            query_vector = self.hyde.create_embedding(
                query
            )

            return self.retrieval.search_vector(
                query_vector,
                query=query,
                top_k=top_k,
            )

        return self.retrieval.hybrid_retrieve(
            query=query,
            top_k=top_k,
        )