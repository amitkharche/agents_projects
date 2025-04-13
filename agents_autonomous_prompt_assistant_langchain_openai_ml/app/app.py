
"""
Streamlit app for Autonomous Prompt-Based Assistant using LangChain Agent.
"""

import os
import sys
import streamlit as st

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

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
