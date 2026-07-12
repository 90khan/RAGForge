import numpy as np

from sentence_transformers import SentenceTransformer

from config.settings import settings

from providers.embedding_provider import EmbeddingProvider


class SentenceTransformerProvider(
    EmbeddingProvider
):

    def __init__(self):

        self.model = SentenceTransformer(
            settings.embedding_model
        )

    def embed(
        self,
        texts,
    ) -> np.ndarray:

        return self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )