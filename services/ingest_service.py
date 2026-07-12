from loaders.pdf_loader import PDFLoader

from core.chunker import TextChunker

from core.embeddings import EmbeddingModel

from vectorstore.faiss_store import FAISSStore


class IngestService:

    def __init__(self):

        self.loader = PDFLoader()

        self.chunker = TextChunker()

        self.embedding = EmbeddingModel()

        self.store = None

    def ingest(
        self,
        pdf_path,
    ):

        text = self.loader.load(
            pdf_path
        )

        chunks = self.chunker.split(
            text
        )

        embeddings = self.embedding.encode(
            chunks
        )

        self.store = FAISSStore(
            embeddings.shape[1]
        )

        self.store.add(
            embeddings,
            chunks,
        )

        return len(chunks)