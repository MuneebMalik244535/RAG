import chromadb
client = chromadb.Client()
collection = client.create_collection("docs")
collection.add(
    documents=[
        "AI is the future",
        "Python is a programming language",
        "RAG is a technique for improving AI",
        "AI is best for automation"
    ],
    ids=["1","2","3","4"]
)
result = collection.query(
    query_texts=["AI"],
    n_results=2
)
print(result)

