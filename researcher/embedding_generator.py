from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, documents):
        # documents is a list of dicts: {'filename':..., 'text':...}
        texts = [doc['text'] for doc in documents]
        embeddings = self.model.encode(texts, convert_to_tensor=True)
        return embeddings
