from pathlib import Path

from core.chunker import TextChunker

from loaders.loader_factory import LoaderFactory

from providers.embedding_factory import (
    EmbeddingFactory,
)

from retrieval.multi_vector.index import (
    MultiVectorIndex,
)


pdf = Path(
    "data/uploads/example.pdf"
)

loader = LoaderFactory.create(
    pdf
)

document = loader.load(
    pdf
)

chunker = TextChunker()

document = chunker.split(
    document
)

embedding = EmbeddingFactory.create()

index = MultiVectorIndex(
    embedding
)

store = index.build(
    document.chunks
)

query = embedding.embed_query(
    "What is RAG?"
)

results = store.search(
    query,
    top_k=5,
)

for r in results:

    print(

        r.score,

        r.chunk.id,

    )