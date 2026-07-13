from evaluation.benchmark import Benchmark
from evaluation.dataset import EvaluationSample

benchmark = Benchmark()

benchmark.add(
    EvaluationSample(
        question="What is RAG?",
        relevant_chunk_ids=["0"],
    )
)

benchmark.add(
    EvaluationSample(
        question="Explain FAISS",
        relevant_chunk_ids=["3"],
    )
)

print(benchmark.samples)
