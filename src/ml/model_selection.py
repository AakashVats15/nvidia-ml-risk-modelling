import pandas as pd
from sklearn.model_selection import TimeSeriesSplit

def split_data(df: pd.DataFrame, n=5):
    tscv = TimeSeriesSplit(n)
    return tscv.split(df)