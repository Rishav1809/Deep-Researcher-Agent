from researcher.embedding_generator import EmbeddingGenerator
from researcher.retriever import Retriever
from researcher.reasoning import Reasoner
from researcher.summarizer import Summarizer
from utils.file_loader import FileLoader
import os

# Load documents
docs_path = os.path.join("data", "docs")
files = FileLoader.load_files(docs_path)  # Returns list of dicts: {'filename':..., 'text':...}

# Generate embeddings
embedder = EmbeddingGenerator()
vectors = embedder.generate_embeddings(files)

# Initialize Retriever, Summarizer, Reasoner
retriever = Retriever(vectors, files)  # Pass both vectors and documents
summarizer = Summarizer()
reasoner = Reasoner()

print("🚀 Deep Researcher Agent Started\n")

while True:
    query = input("Enter your research query (or type 'exit'): ").strip()
    if query.lower() == "exit":
        print("Exiting Deep Researcher Agent...")
        break

    # Retrieve relevant documents
    relevant_docs = retriever.retrieve(query, top_k=3)

    # Multi-step reasoning (for demo, simply returns document texts)
    reasoning_steps = reasoner.analyze(query, relevant_docs)

    # Summarize the findings
    summary = summarizer.summarize(reasoning_steps)

    print("\n--- Research Summary ---")
    print(summary)
    print("------------------------\n")
