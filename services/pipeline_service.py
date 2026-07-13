from pathlib import Path

from core.chunker import TextChunker
from core.llm import LLM

from loaders.loader_factory import LoaderFactory

from services.index_service import IndexService
from services.qa_service import QAService
from services.retrieval_service import RetrievalService


class PipelineService:

    def __init__(self):

        self.qa: QAService | None = None

        self.current_document: Path | None = None

    # -----------------------------------------
    # Index document
    # -----------------------------------------

    def index(
        self,
        file_path: Path,
    ) -> QAService:

        # -------------------------
        # Load
        # -------------------------

        loader = LoaderFactory.create(file_path)

        document = loader.load(file_path)

        # -------------------------
        # Chunk
        # -------------------------

        document = TextChunker().split(document)

        # -------------------------
        # Build indexes
        # -------------------------

        index = IndexService().build(document)

        # -------------------------
        # Retrieval
        # -------------------------

        retriever = RetrievalService(
            store=index.vector_store,
            embedding_provider=index.embedding_provider,
            bm25=index.bm25,
            graph_store=index.graph,
        )

        # -------------------------
        # LLM
        # -------------------------

        llm = LLM()

        self.qa = QAService(
            retriever=retriever,
            llm=llm,
        )

        self.current_document = file_path

        return self.qa

    # -----------------------------------------
    # Backward compatibility
    # -----------------------------------------

    def build(
        self,
        file_path: Path,
    ) -> QAService:

        return self.index(file_path)

    # -----------------------------------------
    # Chat
    # -----------------------------------------

    def chat(
        self,
        question: str,
    ):

        if self.qa is None:

            raise RuntimeError("No document has been indexed.")

        return self.qa.ask(question)

    # -----------------------------------------
    # Status
    # -----------------------------------------

    def is_ready(
        self,
    ) -> bool:

        return self.qa is not None
