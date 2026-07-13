import re

from retrieval.query_expansion_rules import (
    QUERY_EXPANSION,
)


class QueryExpander:

    def expand(
        self,
        query: str,
        include_related: bool = True,
    ) -> str:

        expanded = []

        seen = set()

        words = re.findall(
            r"\w+",
            query.lower(),
        )

        for word in words:

            if word not in seen:

                expanded.append(word)
                seen.add(word)

            rule = QUERY_EXPANSION.get(word)

            if rule is None:
                continue

            # Synonyms
            for synonym in rule.get(
                "synonyms",
                [],
            ):

                if synonym not in seen:

                    expanded.append(synonym)
                    seen.add(synonym)

            # Related terms
            if include_related:

                for related in rule.get(
                    "related",
                    [],
                ):

                    if related not in seen:

                        expanded.append(related)
                        seen.add(related)

        return " ".join(expanded)
