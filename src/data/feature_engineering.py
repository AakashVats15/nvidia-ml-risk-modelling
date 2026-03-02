import pandas as pd

def add_features(df: pd.DataFrame):
    df = df.copy()
    df["LogReturn"] = (df["Close"] / df["Close"].shift(1)).apply(lambda x: pd.NA if x <= 0 else pd.np.log(x))
    df = df.dropna()
    return df
