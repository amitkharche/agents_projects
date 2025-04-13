
"""
Model training script to create LangChain vector store using OpenAI embeddings.
"""

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import pandas as pd
import os

# Manually define your OpenAI API key (POC only)
OPENAI_API_KEY = "openaiapikey

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
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectordb = FAISS.from_documents(split_docs, embeddings)
    vectordb.save_local(VECTOR_DIR)
    print(f"✅ Vector store saved to: {VECTOR_DIR}")

if __name__ == "__main__":
    create_vector_store()
