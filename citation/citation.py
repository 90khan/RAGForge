from dataclasses import dataclass


@dataclass(slots=True)
class Citation:
    """
    Represents a citation for a retrieved chunk.
    """

    id: int

    source: str

    page: int | None

    score: float

    retriever: str