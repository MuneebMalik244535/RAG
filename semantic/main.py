from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
text1 = model.encode(["Today is beautiful day"])
text2 = model.encode(["Artificial Intelligence"])
score = cosine_similarity(text1 , text2)
print(score)