import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_income_column(df):
    df['Income'] = df['Income'].astype(str).str.replace(r'[^\d.]', '', regex=True)
    df['Income'] = pd.to_numeric(df['Income'], errors='coerce')
    return df

def standardize_country_names(df):
    replacements = {
        'USA': 'United States',
        'U.S.': 'United States',
        'UK': 'United Kingdom'
    }
    df['Country'] = df['Country'].replace(replacements)
    return df

def drop_duplicates(df):
    return df.drop_duplicates()