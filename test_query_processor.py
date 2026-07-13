from retrieval.query_processor import QueryProcessor

processor = QueryProcessor()

queries = [
    "What is Retrieval Augmented Generation?",
    "Explain the Vector Database",
    "What is the role of FAISS?",
]

for q in queries:

    print("------------------")

    print(q)

    print(processor.process(q))
