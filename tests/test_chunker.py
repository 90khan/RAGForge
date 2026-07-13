from pathlib import Path

from core.chunker import TextChunker
from loaders.loader_factory import LoaderFactory


def test_chunker():

    pdf = Path("data/uploads/example.pdf")

    loader = LoaderFactory.create(pdf)

    document = loader.load(pdf)

    document = TextChunker().split(document)

    assert len(document.chunks) > 0

    assert len(document.chunks[0].text) > 0
