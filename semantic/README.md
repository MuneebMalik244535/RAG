# Semantic Similarity

This folder demonstrates **Semantic Similarity**, which measures how similar two sentences are based on their meaning, not just their spelling.

### How does Semantic Similarity work?
It uses embeddings to compare two sentences. If the sentences talk about similar topics (e.g., "Artificial Intelligence" and "Machine Learning"), their similarity score will be high (close to 1.0). If they are completely different, the score will be low (close to 0.0).

### How the Code Works (`main.py`):
1. **Loads the Model**: It loads the `"all-MiniLM-L6-v2"` model to generate embeddings.
2. **Encodes Sentences**:
   - `text1`: Encodes `"Today is beautiful day"`.
   - `text2`: Encodes `"Artificial Intelligence"`.
3. **Calculates Similarity**: It uses `cosine_similarity` from `scikit-learn` to compare the two vectors.
4. **Prints Score**: Prints the similarity score. Since these sentences are completely unrelated, the score will be very low.

### Requirements:
To run this code, make sure you install:
```bash
pip install sentence-transformers scikit-learn
```
