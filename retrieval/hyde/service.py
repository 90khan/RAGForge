class HyDEService:

    def __init__(
        self,
        generator,
        embedding_provider,
    ):

        self.generator = generator

        self.embedding = embedding_provider

    def create_embedding(
        self,
        query: str,
    ):

        hypothetical = self.generator.generate(
            query
        )

        vector = self.embedding.embed_query(
            hypothetical
        )

        return vector