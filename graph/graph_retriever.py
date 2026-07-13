from graph.entity_extractor import EntityExtractor


class GraphRetriever:

    """
    Retrieves chunks using
    the knowledge graph.
    """

    def __init__(
        self,
        graph_store,
    ):

        self.graph = graph_store

        self.extractor = EntityExtractor()

    def retrieve(
        self,
        query: str,
    ):

        entities = self.extractor.extract_from_text(
            query
        )

        results = []
        seen = set()

        for entity in entities:

            # Direct matches
            for chunk in self.graph.chunks(
                entity
            ):

                if chunk.id not in seen:

                    results.append(chunk)
                    seen.add(chunk.id)

            # Neighbor matches
            for neighbor in self.graph.neighbors(
                entity
            ):

                for chunk in self.graph.chunks(
                    neighbor
                ):

                    if chunk.id not in seen:

                        results.append(chunk)
                        seen.add(chunk.id)

        return results