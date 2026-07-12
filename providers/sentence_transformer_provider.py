from sentence_transformers import SentenceTransformer


class SentenceTransformerProvider:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed_documents(
        self,
        texts: list[str],
    ):

        return self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

    def embed_query(
        self,
        query: str,
    ):

        return self.model.encode(
            query,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )