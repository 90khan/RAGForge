from retrieval.query_processor import QueryProcessor


def test_query_processor():

    processor = QueryProcessor()

    result = processor.process(
        "What is RAG?"
    )

    assert isinstance(result, str)

    assert "rag" in result.lower()