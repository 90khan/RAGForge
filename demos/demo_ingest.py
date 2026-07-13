from pathlib import Path

from core.chunker import TextChunker
from loaders.loader_factory import LoaderFactory
from services.index_service import IndexService


pdf = Path("data/uploads/example.pdf")

loader = LoaderFactory.create(pdf)

document = loader.load(pdf)

document = TextChunker().split(document)

index = IndexService().build(document)

print(f"Chunks: {len(document.chunks)}")
print(f"FAISS vectors: {index.vector_store.index.ntotal}")
print(f"Graph nodes: {index.graph.graph.number_of_nodes()}")
print(f"Graph edges: {index.graph.graph.number_of_edges()}")