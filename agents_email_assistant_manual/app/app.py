"""
Streamlit interface for AI Email Assistant.
"""
import os
import sys

# Dynamically add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import necessary libraries
import streamlit as st
import pandas as pd
from src.email_classifier import classify_email
from src.reply_generator import generate_reply

st.set_page_config(page_title="📬 AI Email Assistant")
st.title("📬 Autonomous Email Assistant")

uploaded_file = st.file_uploader("Upload a CSV file of emails", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    results = []

    for _, row in df.iterrows():
        label = classify_email(row["subject"], row["body"])
        reply = generate_reply(label)
        results.append({
            "sender": row["sender"],
            "subject": row["subject"],
            "classified_as": label,
            "auto_reply": reply
        })

    result_df = pd.DataFrame(results)
    st.dataframe(result_df)
    st.download_button("Download Replies", result_df.to_csv(index=False), file_name="replies.csv", mime="text/csv")
