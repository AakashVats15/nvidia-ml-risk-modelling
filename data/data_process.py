import pandas as pd
import os

RAW_PATH = r"E:\Personal\GitHub\Python Code Repo\nvidia-ml-risk-modelling\data\raw\NVDA.csv"
PROCESSED_PATH = r"E:\Personal\GitHub\Python Code Repo\nvidia-ml-risk-modelling\data\processed\NVDA_processed.csv"

def load_nvda():
    return pd.read_csv(RAW_PATH)

def preprocess(df):
    df = df.copy()
    df["Return"] = df["Close"].pct_change()
    df = df.dropna()
    return df

def save_processed(df):
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

def run():
    df = load_nvda()
    df = preprocess(df)
    save_processed(df)

if __name__ == "__main__":
    run()