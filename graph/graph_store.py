import networkx as nx


class GraphStore:

    def __init__(self):

        self.graph = nx.Graph()

    def add_entity(
        self,
        entity: str,
    ):

        self.graph.add_node(entity)

    def add_relation(
        self,
        source: str,
        target: str,
    ):

        self.graph.add_edge(
            source,
            target,
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