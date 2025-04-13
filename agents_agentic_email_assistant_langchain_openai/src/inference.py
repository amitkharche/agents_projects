import joblib
import pandas as pd

def predict_labels(model_path, texts):
    model = joblib.load(model_path)
    return model.predict(texts)