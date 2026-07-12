from pathlib import Path

from loaders.loader_factory import LoaderFactory
from core.chunker import TextChunker
from services.vector_service import VectorService

loader = LoaderFactory.create(
    Path("data/uploads/example.pdf")
)

document = loader.load(
    Path("data/uploads/example.pdf")
)

document = TextChunker().split(
    document
)

service = VectorService()

store = service.build(
    document
)

query = "What is Retrieval Augmented Generation?"

query_embedding = (
    service.embedding.embed(
        [query]
    )[0]
)

results = store.search(
    query_embedding,
    top_k=3,
)

for i, result in enumerate(results, start=1):
    print(f"\nResult #{i}")
    print(f"Score : {result.score:.4f}")
    print(f"Text  :\n{result.chunk.text[:300]}")
    print("-" * 80)