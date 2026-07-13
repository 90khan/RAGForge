from core.llm import LLM

from providers.embedding_factory import (
    EmbeddingFactory,
)

from retrieval.hyde.generator import (
    HyDEGenerator,
)

from retrieval.hyde.service import (
    HyDEService,
)

llm = LLM()

embedding = EmbeddingFactory.create()

generator = HyDEGenerator(
    llm
)

hyde = HyDEService(
    generator,
    embedding,
)

vector = hyde.create_embedding(
    "What is Retrieval Augmented Generation?"
)

print(vector.shape)