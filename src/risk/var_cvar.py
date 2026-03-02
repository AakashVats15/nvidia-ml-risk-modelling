import pandas as pd
import numpy as np

def var(df: pd.DataFrame, level=0.95):
    return df["Return"].quantile(1 - level)

def cvar(df: pd.DataFrame, level=0.95):
    v = var(df, level)
    return df[df["Return"] <= v]["Return"].mean()