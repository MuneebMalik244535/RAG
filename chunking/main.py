import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
text = open("doc.txt").read()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_text(text)
print(chunks[0])