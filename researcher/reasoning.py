class Reasoner:
    def analyze(self, query, documents):
        # For simplicity, just return the document texts as reasoning steps
        steps = [doc['text'] for doc in documents]
        return steps
