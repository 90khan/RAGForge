from models.document import Chunk


class MultiVectorEncoder:
    """
    Creates multiple textual representations
    for a single chunk.
    """

    def encode(
        self,
        chunk: Chunk,
    ) -> list[str]:

        vectors = []

        # Original chunk
        vectors.append(chunk.text)

        # First sentence as summary
        first_sentence = chunk.text.split(".")[0].strip()

        if first_sentence:

            vectors.append(first_sentence)

        # Source information
        source = chunk.metadata.get("source")

        if source:

            vectors.append(source.stem)

        return vectors
