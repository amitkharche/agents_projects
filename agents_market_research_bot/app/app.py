"""
Streamlit interface for Market Research Bot
"""

import streamlit as st
import pandas as pd
from src.summarizer import summarize_text

st.set_page_config(page_title="📊 Market Research Bot")
st.title("📊 Autonomous Market Research Bot")

uploaded_file = st.file_uploader("Upload a CSV with competitor text data", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    st.subheader("📌 Summaries")
    df["summary"] = df["description"].apply(summarize_text)
    st.write(df[["company", "summary"]])

    st.download_button("Download Summaries", df.to_csv(index=False), file_name="summarized_competitors.csv", mime="text/csv")
