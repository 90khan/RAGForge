from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass
class Chunk:
    id: int
    text: str
    page: int
    metadata: Dict = field(default_factory=dict)


@dataclass
class Document:
    id: str
    source: Path
    text: str
    chunks: List[Chunk] = field(default_factory=list)