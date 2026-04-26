from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, index, texts):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=1)
    return texts[I[0][0]]