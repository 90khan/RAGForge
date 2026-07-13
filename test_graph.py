from pathlib import Path

from core.chunker import TextChunker
from graph.graph_builder import GraphBuilder
from loaders.loader_factory import LoaderFactory


pdf = Path("data/uploads/example.pdf")

loader = LoaderFactory.create(pdf)

document = loader.load(pdf)

chunker = TextChunker()

document = chunker.split(document)

builder = GraphBuilder()

graph = builder.build(
    document.chunks
)

print(

    "Nodes:",

    graph.graph.number_of_nodes(),

)

print(

    "Edges:",

    graph.graph.number_of_edges(),

)

print()

print(

    list(

        graph.graph.nodes()

    )[:20]

)