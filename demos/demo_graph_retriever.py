from pathlib import Path

from core.chunker import TextChunker
from graph.graph_builder import GraphBuilder
from graph.graph_retriever import GraphRetriever
from loaders.loader_factory import LoaderFactory


pdf = Path("data/uploads/example.pdf")

loader = LoaderFactory.create(pdf)

document = loader.load(pdf)

chunker = TextChunker()

document = chunker.split(document)

builder = GraphBuilder()

graph = builder.build(document.chunks)

retriever = GraphRetriever(graph)

results = retriever.retrieve("Explain FAISS")

print(f"Found {len(results)} chunks")

for chunk in results:

    print(chunk.id)
