import pandas as pd

def extract_date_features(df):
    if 'JoinDate' in df.columns:
        df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
        df['JoinYear'] = df['JoinDate'].dt.year
        df['JoinMonth'] = df['JoinDate'].dt.month
    return df