from pathlib import Path

from loaders.loader_factory import LoaderFactory

from core.chunker import TextChunker

from services.embedding_service import (
    EmbeddingService,
)

file = Path(
    "data/uploads/example.pdf"
)

loader = LoaderFactory.create(file)

document = loader.load(file)

chunker = TextChunker()

document = chunker.split(document)

embedding = EmbeddingService()

document = embedding.embed(document)

print(len(document.chunks))

print(document.chunks[0].text[:100])

print(document.chunks[0].embedding.shape)