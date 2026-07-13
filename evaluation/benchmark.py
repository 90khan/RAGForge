from evaluation.dataset import (
    EvaluationSample,
)


class Benchmark:

    def __init__(self):

        self.samples: list[
            EvaluationSample
        ] = []

    def add(
        self,
        sample: EvaluationSample,
    ):

        self.samples.append(
            sample
        )