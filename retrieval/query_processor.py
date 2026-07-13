import re


class QueryProcessor:

    """
    Cleans and normalizes
    user queries before retrieval.
    """

    def process(
        self,
        query: str,
    ) -> str:

        query = query.lower()

        # Remove punctuation
        query = re.sub(
            r"[^\w\s]",
            " ",
            query,
        )

        # Remove multiple spaces
        query = re.sub(
            r"\s+",
            " ",
            query,
        )

        return query.strip()