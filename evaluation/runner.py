from evaluation.metrics import (
    RetrievalMetrics,
)


class EvaluationRunner:

    def run(
        self,
        retriever,
        benchmark,
    ):

        report = []

        for sample in benchmark.samples:

            results = retriever.hybrid_retrieve(sample.question)

            report.append(
                {
                    "question": sample.question,
                    "recall": RetrievalMetrics.recall_at_k(
                        results,
                        sample.relevant_chunk_ids,
                    ),
                    "precision": RetrievalMetrics.precision_at_k(
                        results,
                        sample.relevant_chunk_ids,
                    ),
                    "hit_rate": RetrievalMetrics.hit_rate(
                        results,
                        sample.relevant_chunk_ids,
                    ),
                    "mrr": RetrievalMetrics.mrr(
                        results,
                        sample.relevant_chunk_ids,
                    ),
                }
            )

        return report
