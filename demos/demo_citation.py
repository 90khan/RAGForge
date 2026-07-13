from pathlib import Path

from citation.citation_builder import CitationBuilder
from citation.formatter import CitationFormatter

from models.document import Chunk
from models.search import SearchResult


chunk = Chunk(
    id="1",
    text="FAISS is a vector database.",
    metadata={},
)

results = [
    SearchResult(
        chunk=chunk,
        score=0.93,
        source=Path("example.pdf"),
        page=3,
        retriever="semantic",
    ),
    SearchResult(
        chunk=chunk,
        score=0.88,
        source=Path("example.pdf"),
        page=5,
        retriever="graph",
    ),
]

builder = CitationBuilder()

citations = builder.build(results)

formatter = CitationFormatter()

print(formatter.markdown(citations))
