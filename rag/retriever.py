import faiss
import json
import numpy as np
from llm.ollama_embed import embed

index = faiss.read_index("vector_db/faiss.index")

with open("data/code_chunks.json") as f:
    chunks = json.load(f)

def search(query, k=5):
    q_vec = np.array([embed(query)]).astype("float32")
    D, I = index.search(q_vec, k)

    return [chunks[i]["text"] for i in I[0]]
