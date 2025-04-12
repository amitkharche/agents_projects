"""
LangChain + Pandas-based data cleaning agent logic.
Simulates intelligent detection and correction of common issues.
"""

import pandas as pd
import numpy as np

def detect_issues(df):
    issues = []

    if df.isnull().sum().sum() > 0:
        issues.append("⚠️ Missing values detected.")

    if df.duplicated().any():
        issues.append("⚠️ Duplicate rows found.")

    if "Age" in df.columns and (df["Age"] > 100).any():
        issues.append("⚠️ Outliers in 'Age' column.")

    if "Country" in df.columns:
        issues.append("ℹ️ Non-standard country names: " + ", ".join(df["Country"].unique()))

    if "Income" in df.columns and df["Income"].str.contains(r"\$|K|,", regex=True).any():
        issues.append("⚠️ Non-numeric income formats detected.")

    return issues

def clean_data(df):
    cleaned_df = df.copy()

    if "CustomerID" in df.columns:
        cleaned_df = cleaned_df.drop_duplicates(subset=["CustomerID"])

    if "JoinDate" in df.columns:
        cleaned_df["JoinDate"] = pd.to_datetime(cleaned_df["JoinDate"], errors="coerce")

    if "Income" in df.columns:
        cleaned_df["Income"] = cleaned_df["Income"].replace(r"\$|,", "", regex=True).replace("K", "000", regex=True).astype(str)
        cleaned_df["Income"] = pd.to_numeric(cleaned_df["Income"], errors="coerce")

    if "Country" in df.columns:
        cleaned_df["Country"] = cleaned_df["Country"].str.upper().replace({"USA": "US", "CANADA": "CA", "INDIA": "IN"})

    cleaned_df["Age"] = cleaned_df["Age"].apply(lambda x: np.nan if x and (x < 10 or x > 100) else x)

    return cleaned_df
