from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from models.document import Chunk


@dataclass(slots=True)
class SearchResult:
    """
    Represents a retrieved document chunk.
    """

    chunk: Chunk

    score: float

    source: Path

    page: int | None

    retriever: str = "semantic"

    rank: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )