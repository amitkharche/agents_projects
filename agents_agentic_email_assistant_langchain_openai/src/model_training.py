from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import pandas as pd
import joblib
import os

def train_model(data_path, model_path='models/email_classifier.pkl'):
    df = pd.read_csv(data_path)
    df['text'] = df['subject'].astype(str) + " " + df['body'].astype(str)
    df['label'] = df['subject'].apply(lambda x: 'meeting' if 'meet' in x.lower() else 'report' if 'report' in x.lower() else 'promo')

    X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    param_grid = {'tfidf__max_df': [0.8, 1.0]}
    grid = GridSearchCV(pipeline, param_grid, cv=2)
    grid.fit(X_train, y_train)

    y_pred = grid.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(grid, model_path)
    print(f"✅ Model saved at {model_path}")
    return report

if __name__ == "__main__":
    train_model("data/raw/emails.csv")
