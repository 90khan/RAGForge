from models.document import Document
from providers.embedding_factory import EmbeddingFactory
from vectorstore.faiss_store import FAISSStore


class IndexService:
    """
    Responsible for creating a FAISS index from a Document.

    Document
        ↓
    Embeddings
        ↓
    FAISS
    """

    def __init__(self):

        self.embedding_provider = EmbeddingFactory.create()

        self.store = None

    def build_index(
        self,
        document: Document,
    ) -> FAISSStore:

        texts = [
            chunk.text
            for chunk in document.chunks
        ]

        embeddings = self.embedding_provider.embed_documents(
            texts
        )

        self.store = FAISSStore(
            dimension=embeddings.shape[1]
        )

        self.store.add(
            chunks=document.chunks,
            embeddings=embeddings,
        )

        return self.store