from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from collections import defaultdict
import time
def Question_Answer(querry):
    embeddings= HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore=Chroma(persist_directory='db\\Chroma_db',embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_type='mmr',search_kwargs={'k':6,'fetch_k':20})
    result=retriever.invoke(querry)
    context=""
    sources = defaultdict(set)
    for doc in result:
        context+=doc.page_content+'\n\n'
        file = doc.metadata["source"].split("\\")[-1]
        page = doc.metadata["page"] + 1
        sources[file].add(page)
    prompt = f""" You are a research assistant.
    Provide an answer to the user's question based on the given context ONLY.
    For comparison questions :-
    Compare concepts point by point
    If the context is sufficient enough to partially answer the user's question, provide the answer.
    If the context is not at all relevant to the question, then say:
    "I do not have sufficient information to provide an answer"
    User's Question:
    {querry}
    Context :
    {context}
    Answer:"""
    s=time.time()
    LLM =ChatOllama(model='gemma3:4b',temperature=0,num_predict=500)
    response = LLM.invoke(prompt)
    return response.content, sources

