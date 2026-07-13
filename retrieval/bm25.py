from rank_bm25 import BM25Okapi

from models.document import Chunk
from models.search import SearchResult


class BM25Retriever:

    def __init__(self):

        self.index = None

        self.chunks: list[Chunk] = []

    def build(
        self,
        chunks: list[Chunk],
    ):

        self.chunks = chunks

        corpus = [

            chunk.text.split()

            for chunk in chunks

        ]

        self.index = BM25Okapi(
            corpus
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[SearchResult]:

        scores = self.index.get_scores(
            query.split()
        )

        ranked = sorted(

            zip(
                scores,
                self.chunks,
            ),

            key=lambda item: item[0],

            reverse=True,

        )

        results = []

        for rank, (score, chunk) in enumerate(
            ranked[:top_k],
            start=1,
        ):

            results.append(

                SearchResult(

                    chunk=chunk,

                    score=float(score),

                    source=chunk.metadata["source"],

                    page=chunk.metadata.get(
                        "page"
                    ),

                    retriever="bm25",

                    rank=rank,

                )

            )

        return results