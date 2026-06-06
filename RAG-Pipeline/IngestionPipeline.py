from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def Loadfiles(path):
    loader = PyPDFDirectoryLoader(path)
    doc= loader.load()
    return doc

def FileSplitter(docs):
    Splitter=RecursiveCharacterTextSplitter(chunk_size=1000,
      chunk_overlap=200,
      add_start_index=True,
    )
    ChunkedDoc=Splitter.split_documents(docs)
    return ChunkedDoc
doc=Loadfiles("data\\")
chunk = FileSplitter(doc)


embedding_model = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
print("Creating Vector Store and embedding documents")
vectorstore = Chroma.from_documents(documents=chunk,
                                    embedding=embedding_model,
                                    persist_directory='db\\Chroma_db')





   


