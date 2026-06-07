# ChromaDB Vector Database

This folder demonstrates **ChromaDB**, which is an open-source vector database used to store and search text embeddings.

### Why do we need a Vector Database?
In RAG (Retrieval-Augmented Generation), we need to search through thousands of document chunks instantly. ChromaDB stores our documents and their embeddings, allowing us to perform fast semantic searches.

### How the Code Works (`main.py`):
1. **Initializes Client**: It starts an in-memory ChromaDB client.
2. **Creates Collection**: It creates a collection (like a table in SQL) named `"docs"`.
3. **Adds Documents**: It inserts 4 document chunks into the collection and assigns them unique IDs (`"1"`, `"2"`, `"3"`, `"4"`).
4. **Queries Database**: It searches the collection for documents semantically closest to the query `"AI"`.
5. **Prints Results**: Prints the top 2 matching documents (`n_results=2`).

### Requirements:
To run this code, make sure you install:
```bash
pip install chromadb
```
