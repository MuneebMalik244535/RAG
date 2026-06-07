import os
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
text = "Artificial Intelligene is the future of automation."
embedding = model.encode(text)
print(len(embedding))
print(embedding[:10])

