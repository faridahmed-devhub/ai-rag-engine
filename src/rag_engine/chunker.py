from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


class TextChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=80
        )


    def split(self, text):

        return self.splitter.split_text(text)
