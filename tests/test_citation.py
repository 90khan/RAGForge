from pathlib import Path

from citation.citation_builder import CitationBuilder
from models.document import Chunk
from models.search import SearchResult


def test_citation_builder():

    chunk = Chunk(
        id="1",
        text="Hello World",
        metadata={
            "source": Path("example.pdf"),
            "page": 3,
        },
    )

    result = SearchResult(
        chunk=chunk,
        score=0.9,
        source=Path("example.pdf"),
        page=3,
        retriever="semantic",
    )

    citations = CitationBuilder().build([result])

    assert len(citations) == 1

    assert citations[0].page == 3
