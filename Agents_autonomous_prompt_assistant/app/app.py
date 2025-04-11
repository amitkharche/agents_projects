"""
Streamlit frontend for company-specific assistant using LangChain agent.
"""

import streamlit as st
from src.agent import load_qa_chain

st.set_page_config(page_title="🤖 Company Assistant", layout="centered")
st.title("🤖 Ask your Company Assistant")

qa_chain = load_qa_chain()

query = st.text_input("What would you like to know?")
if query:
    with st.spinner("Thinking..."):
        response = qa_chain.run(query)
    st.success("Response:")
    st.write(response)
