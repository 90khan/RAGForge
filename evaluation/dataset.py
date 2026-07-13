from dataclasses import dataclass


@dataclass(slots=True)
class EvaluationSample:
    """
    One benchmark sample.
    """

    question: str

    relevant_chunk_ids: list[str]
