import pandas as pd
from src.data.load_data import load_nvda
from src.data.preprocess import preprocess
from src.ml.model_training import train_model
from src.ml.risk_prediction import predict_risk

def run_forecasting_pipeline(path="data/raw/NVDA.csv"):
    df = load_nvda(path)
    df = preprocess(df)
    m = train_model(df)
    preds = predict_risk(m, df)
    return df, m, preds