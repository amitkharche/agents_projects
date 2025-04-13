import os
import sys
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
#from langchain.agents import create_pandas_dataframe_agent
from langchain_experimental.agents import create_pandas_dataframe_agent


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.preprocessing import clean_income_column, standardize_country_names, drop_duplicates
from src.feature_engineering import extract_date_features
from src.utils import load_openai_key

st.set_page_config(page_title="🧠 AI Data Cleaning Agent")
st.title("🧠 AI-Powered Data Cleaning Assistant")

load_dotenv()
#OPENAI_API_KEY = load_openai_key() #Load key from .env
OPENAI_API_KEY = "sk-api_key"

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Raw Data")
    st.dataframe(df)

    st.write("Performing Rule-based Cleaning...")
    df = clean_income_column(df)
    df = standardize_country_names(df)
    df = drop_duplicates(df)
    df = extract_date_features(df)

    st.subheader("✅ Cleaned Data")
    st.dataframe(df)

    st.write("🔍 Running AI-powered Data Insights...")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)
    agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True)

    issues = agent.run("List the data quality issues and suggested fixes.")
    st.subheader("🧠 AI Feedback")
    st.write(issues)