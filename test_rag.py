from pathlib import Path

from loaders.loader_factory import LoaderFactory

from core.chunker import TextChunker

from services.retrieval_service import RetrievalService
from services.qa_service import QAService

from core.llm import LLM
from services.index_service import IndexService


pdf = Path("data/uploads/example.pdf")

loader = LoaderFactory.create(pdf)

document = loader.load(pdf)

document = TextChunker().split(document)



index = IndexService()

store = index.build_index(
    document
)

retriever = RetrievalService(
    store=store,
    embedding_provider=index.embedding_provider,
    bm25=index.bm25,
)

llm = LLM()

qa = QAService(
    retriever,
    llm,
)

while True:

    question = input("\nQuestion : ")

    if question.lower() == "exit":
        break

    print()

    print(

        qa.ask(question)

    )