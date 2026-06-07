# Document Chunking

This folder demonstrates **Document Chunking**, which is the process of breaking down large documents into smaller, manageable text chunks.

### Why do we need Chunking?
Large documents cannot be sent to Large Language Models (LLMs) all at once because of context window limits. Chunking helps break down text so we can find and retrieve only the most relevant parts for a query.

### How the Code Works (`main.py`):
1. **Reads File**: It opens and reads the text from `doc.txt`.
2. **Text Splitter**: It initializes `RecursiveCharacterTextSplitter` from LangChain:
   - `chunk_size=500`: Each chunk will have a maximum of 500 characters.
   - `chunk_overlap=50`: The next chunk will start with 50 overlapping characters from the previous chunk. This ensures no context is lost at the boundaries.
3. **Splits & Prints**: It splits the document into chunks and prints the first chunk (`chunks[0]`).

### Requirements:
To run this code, make sure you install:
```bash
pip install langchain-text-splitters
```
