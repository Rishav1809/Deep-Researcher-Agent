from sentence_transformers import SentenceTransformer
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, vectors, documents):
        self.vectors = vectors
        self.documents = documents

    def retrieve(self, query, top_k=3):
        # Convert query to embedding
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_vec = model.encode([query], convert_to_tensor=True)

        # Compute cosine similarity
        sims = cosine_similarity(query_vec.cpu().numpy(), self.vectors.cpu().numpy())[0]

        # Get top_k indices
        top_indices = np.argsort(sims)[-top_k:][::-1]
        top_docs = [self.documents[i] for i in top_indices]
        return top_docs
