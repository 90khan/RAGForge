from pathlib import Path

from core.chunker import TextChunker
from graph.graph_builder import GraphBuilder
from loaders.loader_factory import LoaderFactory


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

builder = GraphBuilder()

graph = builder.build(
    document.chunks
)

print(
    f"Nodes : {graph.graph.number_of_nodes()}"
)

print(
    f"Edges : {graph.graph.number_of_edges()}"
)

print()

print("First 20 entities")

for entity in list(graph.graph.nodes())[:20]:

    print(
        "-",
        entity,
    )

print()

print("Entity -> Chunk Mapping")

count = 0

for entity, chunks in graph.entity_chunks.items():

    ids = sorted(
        chunk.id
        for chunk in chunks
    )

    print(
        entity,
        "->",
        ids,
    )

    count += 1

    if count == 10:
        break