from services.vector_service import VectorService


class RetrievalService:

    def __init__(self, store, embedding_provider):

        self.store = store
        self.embedding = embedding_provider

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_embedding = self.embedding.embed(
            [query]
        )[0]

        return self.store.search(
            query_embedding,
            top_k=top_k,
        )