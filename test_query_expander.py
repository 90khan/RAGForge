from retrieval.query_expander import QueryExpander

expander = QueryExpander()

tests = [

    "What is RAG?",

    "Explain FAISS.",

    "What is BM25?",

    "How does Graph RAG work?",

]

for query in tests:

    print("-" * 60)

    print("Original :", query)

    print("Expanded :", expander.expand(query))