from retrieval.query_expander import QueryExpander


def test_query_expander():

    expander = QueryExpander()

    result = expander.expand(
        "What is RAG?"
    )

    assert isinstance(result, str)

    assert len(result) > len("What is RAG?")

    assert "rag" in result.lower()