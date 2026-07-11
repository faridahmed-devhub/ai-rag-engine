import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatIP(
            dimension
        )


    def add(self, vectors):

        self.index.add(
            np.array(vectors)
        )


    def search(self, vector, k=5):

        return self.index.search(
            np.array([vector]),
            k
        )
