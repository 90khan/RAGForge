from citation.citation import Citation

from models.search import SearchResult


class CitationBuilder:

    def build(
        self,
        results: list[SearchResult],
    ) -> list[Citation]:

        citations = []

        for index, result in enumerate(
            results,
            start=1,
        ):

            citations.append(

                Citation(

                    id=index,

                    source=result.source.name,

                    page=result.page,

                    score=result.score,

                    retriever=result.retriever,

                )

            )

        return citations