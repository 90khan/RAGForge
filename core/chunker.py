from models.document import Chunk, Document


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ):

        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(
        self,
        document: Document,
    ) -> Document:

        document.chunks.clear()

        text = document.text.strip()

        if not text:
            return document

        step = self.chunk_size - self.overlap

        chunk_id = 0

        for start in range(0, len(text), step):

            end = start + self.chunk_size

            chunk_text = text[start:end].strip()

            if not chunk_text:
                continue

            chunk = Chunk(
                id=str(chunk_id),
                text=chunk_text,
                metadata={
                    "source": document.source,
                    "page": None,
                    "chunk": chunk_id,
                    "start": start,
                    "end": end,
                },
            )

            document.chunks.append(chunk)

            chunk_id += 1

            if end >= len(text):
                break

        return document