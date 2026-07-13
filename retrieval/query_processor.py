import re


class QueryProcessor:

    def __init__(self):

        self.stopwords = {

            "the",
            "a",
            "an",
            "is",
            "are",
            "of",
            "to",
            "for",
            "and",
            "or",
            "in",

        }

    def normalize(
        self,
        query: str,
    ) -> str:

        query = query.lower()

        query = re.sub(
            r"\s+",
            " ",
            query,
        )

        return query.strip()

    def remove_stopwords(
        self,
        query: str,
    ) -> str:

        words = query.split()

        words = [

            w

            for w in words

            if w not in self.stopwords

        ]

        return " ".join(words)

    def process(
        self,
        query: str,
    ) -> str:

        query = self.normalize(
            query
        )

        query = self.remove_stopwords(
            query
        )

        return query