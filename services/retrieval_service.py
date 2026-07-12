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
        query,
        top_k=5,
        min_score=0.55,
    ):

        vector = self.embedding.embed([query])[0]

        results = self.store.search(
            vector,
            top_k,
        )

        return [

            r

            for r in results

            if r.score >= min_score

        ]