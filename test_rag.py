from pathlib import Path

from loaders.loader_factory import LoaderFactory

from core.chunker import TextChunker

from services.vector_service import VectorService
from services.retrieval_service import RetrievalService
from services.qa_service import QAService

from core.llm import LLM


pdf = Path("data/uploads/example.pdf")

loader = LoaderFactory.create(pdf)

document = loader.load(pdf)

document = TextChunker().split(document)

vector = VectorService()

store = vector.build(document)

retriever = RetrievalService(
    store,
    vector.embedding,
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