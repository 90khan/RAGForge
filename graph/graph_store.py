from collections import defaultdict

import networkx as nx


class GraphStore:

    def __init__(self):

        self.graph = nx.Graph()

        # entity -> list[Chunk]
        self.entity_chunks = defaultdict(list)

    def add_entity(
        self,
        entity: str,
    ):

        self.graph.add_node(
            entity
        )

    def add_relation(
        self,
        source: str,
        target: str,
    ):

        self.graph.add_edge(
            source,
            target,
        )

    def add_chunk(
        self,
        entity: str,
        chunk,
    ):

        chunks = self.entity_chunks[
            entity
        ]

        # Avoid duplicates
        if all(
            c.id != chunk.id
            for c in chunks
        ):

            chunks.append(
                chunk
            )

    def neighbors(
        self,
        entity: str,
    ):

        if entity not in self.graph:

            return []

        return list(
            self.graph.neighbors(
                entity
            )
        )

    def chunks(
        self,
        entity: str,
    ):

        return self.entity_chunks.get(
            entity,
            [],
        )