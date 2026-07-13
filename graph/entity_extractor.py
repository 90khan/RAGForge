import re

from models.document import Chunk


class EntityExtractor:

    """
    Very lightweight entity extractor.

    Later this class can be replaced
    by spaCy or an LLM.
    """

    def extract(
        self,
        chunk: Chunk,
    ) -> list[str]:

        entities = []

        words = re.findall(
            r"\b[A-Z][a-zA-Z0-9_-]+\b",
            chunk.text,
        )

        seen = set()

        for word in words:

            if word in seen:
                continue

            seen.add(word)
            entities.append(word)

        return entities