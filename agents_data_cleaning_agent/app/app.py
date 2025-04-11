"""
Streamlit app with extended support for Excel, JSON, and XML files.
"""

import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from io import StringIO
from src.data_cleaning_agent import detect_issues, clean_data

st.set_page_config(page_title="🧹 Universal Data Cleaning Agent")
st.title("🧹 AI Data Cleaning Agent")

def read_uploaded_file(uploaded_file, file_type):
    if file_type == "csv":
        return pd.read_csv(uploaded_file)
    elif file_type == "excel":
        return pd.read_excel(uploaded_file)
    elif file_type == "json":
        return pd.read_json(uploaded_file)
    elif file_type == "xml":
        xml_str = uploaded_file.read().decode("utf-8")
        root = ET.fromstring(xml_str)
        data = []
        for child in root:
            data.append({elem.tag: elem.text for elem in child})
        return pd.DataFrame(data)
    else:
        return None

file_type = st.selectbox("Select file type", ["csv", "excel", "json", "xml"])
uploaded_file = st.file_uploader("Upload your data file", type=[file_type])

if uploaded_file:
    df = read_uploaded_file(uploaded_file, file_type)
    if df is not None:
        st.subheader("🔍 Detected Issues")
        issues = detect_issues(df)
        for issue in issues:
            st.write(issue)

        st.subheader("🧼 Cleaned Data")
        cleaned_df = clean_data(df)
        st.dataframe(cleaned_df)

        st.download_button("Download Cleaned CSV", cleaned_df.to_csv(index=False), file_name="cleaned_data.csv", mime="text/csv")
    else:
        st.error("Unable to read the uploaded file.")
