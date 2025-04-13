import os
import sys

# Dynamically add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import joblib
from src.utils import load_openai_key
from src.inference import predict_labels
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# Page settings
st.set_page_config(page_title="📧 AI Email Assistant")
st.title("📧 AI Email Assistant: Smart Classification + Agentic GPT Replies")

# Load OpenAI API key
load_dotenv()
#api_key = load_openai_key()
api_key = st.text_input("Enter your OpenAI API key", type="password")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV with sender, subject, body", type=["csv"])

if uploaded_file and api_key:
    df = pd.read_csv(uploaded_file)
    df['text'] = df['subject'].astype(str) + " " + df['body'].astype(str)

    # ML-Based classification
    st.subheader("📌 ML-Based Classification")
    df['ML_Label'] = predict_labels("models/email_classifier.pkl", df['text'])
    st.dataframe(df[['sender', 'subject', 'ML_Label']])

    # LangChain Agent setup
    st.subheader("🧠 GPT-Powered Agentic Reply")

    llm = ChatOpenAI(temperature=0.5, openai_api_key=api_key)

    def reply_tool_fn(input_text):
        prompt = f"""Write a polite and professional reply to this email:

{input_text}"""
        return llm.predict(prompt)

    tools = [
        Tool(
            name="ReplyGenerator",
            func=reply_tool_fn,
            description="Generates a polite and professional reply to an email"
        )
    ]

    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

    df['AI_Reply'] = df['text'].apply(lambda x: agent.run(f"Reply to this email: {x}"))
    st.dataframe(df[['subject', 'ML_Label', 'AI_Reply']])
    st.download_button("Download Replies", df.to_csv(index=False), "email_replies.csv", "text/csv")
