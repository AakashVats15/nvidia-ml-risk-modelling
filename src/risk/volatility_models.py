import pandas as pd

def realized_vol(df: pd.DataFrame, window=21):
    return df["Return"].rolling(window).std()