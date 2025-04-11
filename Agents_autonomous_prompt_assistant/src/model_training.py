"""
LangChain vector store and agent setup for Autonomous Prompt-Based Assistant.
"""

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
import pandas as pd
import os

DATA_PATH = "data/raw/company_faq.csv"
VECTOR_DIR = "models/vector_store"

def load_docs():
    df = pd.read_csv(DATA_PATH)
    docs = [Document(page_content=f"Q: {row['question']}\nA: {row['answer']}") for _, row in df.iterrows()]
    return docs

def create_vector_store():
    docs = load_docs()
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_documents(split_docs, embeddings)
    vectordb.save_local(VECTOR_DIR)
    return vectordb

def load_qa_chain():
    vectordb = FAISS.load_local(VECTOR_DIR, OpenAIEmbeddings())
    llm = ChatOpenAI(temperature=0.3)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qa
