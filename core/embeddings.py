from sentence_transformers import SentenceTransformer

from config.settings import settings


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(settings.embedding_model)

    def encode(self, texts):

        return self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )
