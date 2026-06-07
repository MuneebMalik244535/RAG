# Text Embeddings

This folder demonstrates **Text Embeddings**, which represent the meaning of text in the form of numbers.

### What are Embeddings?
Computers cannot understand raw words directly. Embeddings convert text into a list of numbers (a vector) where sentences with similar meanings have similar numbers.

### How the Code Works (`main.py`):
1. **Loads the Model**: It imports `SentenceTransformer` and loads the pre-trained `"all-MiniLM-L6-v2"` model.
2. **Generates Embedding**: It encodes the sentence `"Artificial Intelligene is the future of automation."` into a numerical vector.
3. **Prints Information**:
   - `len(embedding)`: Prints the length of the vector (384 dimensions for this model).
   - `embedding[:10]`: Prints the first 10 numbers of the generated vector.

### Requirements:
To run this code, make sure you install:
```bash
pip install sentence-transformers
```
