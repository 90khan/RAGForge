from pathlib import Path

from core.chunker import TextChunker
from loaders.loader_factory import LoaderFactory

from providers.embedding_factory import (
    EmbeddingFactory,
)

from retrieval.multi_vector.index import (
    MultiVectorIndex,
)


pdf_path = Path(
    "data/uploads/example.pdf"
)

loader = LoaderFactory.create(
    pdf_path
)

document = loader.load(
    pdf_path
)

chunker = TextChunker()

document = chunker.split(
    document
)

embedding = EmbeddingFactory.create()

index = MultiVectorIndex(
    embedding_provider=embedding
)

vectors = index.build(
    document.chunks
)

print(
    f"{len(document.chunks)} chunks"
)

print(
    f"{len(vectors)} indexed chunks"
)

for chunk_id, embeddings in vectors.items():

    print(
        f"Chunk {chunk_id}: {len(embeddings)} vectors"
    )