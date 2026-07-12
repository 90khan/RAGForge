from dataclasses import dataclass
from pathlib import Path

from models.document import Chunk


@dataclass(slots=True)
class SearchResult:
    chunk: Chunk
    score: float
    source: Path
    page: int | None