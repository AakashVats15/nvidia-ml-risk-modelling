import pandas as pd
import numpy as np

def tail_ratio(df: pd.DataFrame):
    pos = df[df["Return"] > 0]["Return"].mean()
    neg = df[df["Return"] < 0]["Return"].mean()
    return pos / abs(neg)