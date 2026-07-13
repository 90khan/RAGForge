from typing import Optional

from graph.graph_builder import GraphBuilder

from models.document import Document

from providers.embedding_factory import EmbeddingFactory

from retrieval.bm25 import BM25Retriever
from retrieval.multi_vector.index import MultiVectorIndex

from vectorstore.faiss_store import FAISSStore


class IndexService:
    """
    Responsible for building every retrieval index.

    Document
        │
        ├── FAISS
        ├── BM25
        ├── Graph
        └── Multi-Vector
    """

    def __init__(self):

        self.embedding_provider = (
            EmbeddingFactory.create()
        )

        self.vector_store: Optional[FAISSStore] = None

        self.multi_vector_store = None

        self.graph = None

        self.bm25 = BM25Retriever()

    def build(
        self,
        document: Document,
    ) -> "IndexService":

        texts = [
            chunk.text
            for chunk in document.chunks
        ]

        embeddings = self.embedding_provider.embed_documents(
            texts
        )

        # ---------------------------------
        # FAISS
        # ---------------------------------

        self.vector_store = FAISSStore(
            dimension=embeddings.shape[1]
        )

        self.vector_store.add(
            chunks=document.chunks,
            embeddings=embeddings,
        )

        # ---------------------------------
        # BM25
        # ---------------------------------

        self.bm25.build(
            document.chunks
        )

        # ---------------------------------
        # Knowledge Graph
        # ---------------------------------

        self.graph = GraphBuilder().build(
            document.chunks
        )

        # ---------------------------------
        # Multi Vector
        # ---------------------------------

        self.multi_vector_store = (
            MultiVectorIndex(
                self.embedding_provider
            ).build(
                document.chunks
            )
        )

        return self