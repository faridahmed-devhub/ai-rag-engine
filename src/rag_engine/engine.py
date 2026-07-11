from .chunker import TextChunker
from .embeddings import EmbeddingModel


class RAGEngine:

    def __init__(self):

        self.chunker = TextChunker()
        self.embedding = EmbeddingModel()

        self.documents = []


    def ingest(self, text):

        chunks = self.chunker.split(text)

        vectors = self.embedding.encode(
            chunks
        )

        self.documents.extend(
            zip(chunks, vectors)
        )


    def search(self, query):

        return []
