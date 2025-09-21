import streamlit as st
from researcher.embedding_generator import EmbeddingGenerator
from researcher.retriever import Retriever
from researcher.reasoning import Reasoner
from researcher.summarizer import Summarizer
from utils.file_loader import FileLoader
import os

st.title("Deep Researcher Agent")

# Load documents
docs_path = os.path.join("data", "docs")
files = FileLoader.load_files(docs_path)

# Generate embeddings
embedder = EmbeddingGenerator()
vectors = embedder.generate_embeddings(files)
retriever = Retriever(vectors, files)

# Summarizer and reasoning
summarizer = Summarizer()
reasoner = Reasoner()

query = st.text_input("Enter your research query")
if query:
    relevant_docs = retriever.retrieve(query)
    reasoning_steps = reasoner.analyze(query, relevant_docs)
    summary = summarizer.summarize(reasoning_steps)
    st.subheader("Research Summary")
    st.write(summary)
