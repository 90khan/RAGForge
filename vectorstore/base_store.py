from abc import ABC, abstractmethod

from models.document import Chunk
from models.search import SearchResult


class BaseVectorStore(ABC):

    @abstractmethod
    def add(
        self,
        chunks: list[Chunk],
        embeddings,
    ) -> None:
        ...

    @abstractmethod
    def search(
        self,
        embedding,
        top_k: int,
    ) -> list[SearchResult]:
        ...