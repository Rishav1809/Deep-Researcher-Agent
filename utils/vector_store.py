import os
import pickle
import numpy as np

class VectorStore:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        os.makedirs(folder_path, exist_ok=True)
        self.vectors_file = os.path.join(folder_path, "vectors.pkl")
        self.docs_file = os.path.join(folder_path, "docs.pkl")

    def save_vectors(self, documents, vectors):
        with open(self.vectors_file, 'wb') as vf:
            pickle.dump(vectors, vf)
        with open(self.docs_file, 'wb') as df:
            pickle.dump(documents, df)

    def load_vectors(self):
        with open(self.vectors_file, 'rb') as vf:
            vectors = pickle.load(vf)
        with open(self.docs_file, 'rb') as df:
            documents = pickle.load(df)
        return vectors, documents
