import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['subject', 'body'], inplace=True)
    return df