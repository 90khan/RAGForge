from dataclasses import dataclass

from models.document import Chunk


@dataclass(slots=True)
class SearchResult:
    chunk: Chunk
    score: float