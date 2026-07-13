from graph.entity_extractor import EntityExtractor
from graph.graph_store import GraphStore


class GraphBuilder:

    def __init__(self):

        self.extractor = EntityExtractor()

    def build(
        self,
        chunks,
    ):

        store = GraphStore()

        for chunk in chunks:

            entities = self.extractor.extract(
                chunk
            )

            # Add entities and map them to the current chunk
            for entity in entities:

                store.add_entity(
                    entity
                )

                store.add_chunk(
                    entity,
                    chunk,
                )

            # Create relationships between entities
            for i in range(len(entities)):

                for j in range(i + 1, len(entities)):

                    store.add_relation(
                        entities[i],
                        entities[j],
                    )

        return store