import re

from models.document import Chunk


class EntityExtractor:

    """
    Lightweight entity extractor.

    Can extract entities from either
    a Chunk or plain text.

    Later this class can be replaced
    by spaCy or an LLM.
    """

    ENTITY_PATTERN = re.compile(
        r"\b[A-Z][a-zA-Z0-9_-]+\b"
    )

    def extract(
        self,
        chunk: Chunk,
    ) -> list[str]:

        return self.extract_from_text(
            chunk.text
        )

    def extract_from_text(
        self,
        text: str,
    ) -> list[str]:

        entities = []

        seen = set()

        words = self.ENTITY_PATTERN.findall(
            text
        )

        for word in words:

            if word in seen:
                continue

            seen.add(word)

            entities.append(
                word
            )

        return entities