from models.document import Chunk, Document


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(
        self,
        document: Document,
    ) -> Document:

        text = document.text

        start = 0

        chunk_id = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = Chunk(
                id=chunk_id,
                text=text[start:end],
            )

            document.chunks.append(chunk)

            chunk_id += 1

            start += self.chunk_size - self.overlap

        return document