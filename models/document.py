from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Chunk:
    id: str
    text: str
    page: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Document:
    id: str
    source: Path
    text: str
    chunks: list[Chunk] = field(default_factory=list)
