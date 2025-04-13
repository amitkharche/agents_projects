def combine_subject_and_body(df):
    df['text'] = df['subject'].astype(str) + " " + df['body'].astype(str)
    return df