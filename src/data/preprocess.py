import pandas as pd

def preprocess(df: pd.DataFrame):
    df = df.copy()
    df["Return"] = df["Close"].pct_change()
    df = df.dropna()
    return df