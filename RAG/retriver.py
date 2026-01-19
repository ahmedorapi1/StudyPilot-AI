from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

emb = OllamaEmbeddings(model='nomic-embed-text')
theory_db = Chroma(persist_directory="theory_db", embedding_function=emb)
questions_db = Chroma(persist_directory="questions_db", embedding_function=emb)


def retrive_theory(query):
    docs = theory_db.similarity_search(query, k=3)
    context = '/n'.join([d.page_content for d in docs])
    return context


def retrive_questions(query):
    docs = questions_db.similarity_search(query, k=3)
    context = '/n'.join([d.page_content for d in docs])
    return context
