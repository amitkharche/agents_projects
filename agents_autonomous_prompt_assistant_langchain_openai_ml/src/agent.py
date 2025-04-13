
"""
LangChain agent loader to interact with saved FAISS vector store.
"""

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Manually define your OpenAI API key (POC only)
OPENAI_API_KEY = "openaiapikey"

VECTOR_DIR = "models/vector_store"

def load_qa_chain():
    #vectordb = FAISS.load_local(VECTOR_DIR, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))
    vectordb = FAISS.load_local(
    VECTOR_DIR,
    OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True)  # ✅ trust yourself)
    llm = ChatOpenAI(temperature=0.3, openai_api_key=OPENAI_API_KEY)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qastreaml
