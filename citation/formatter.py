from citation.citation import Citation


class CitationFormatter:

    def markdown(
        self,
        citations: list[Citation],
    ) -> str:

        if not citations:

            return "No sources."

        lines = []

        for citation in citations:

            page = citation.page if citation.page is not None else "-"

            lines.append(
                f"[{citation.id}] "
                f"{citation.source} "
                f"(Page {page}) "
                f"Score: {citation.score:.3f} "
                f"[{citation.retriever}]"
            )

        return "\n".join(lines)
