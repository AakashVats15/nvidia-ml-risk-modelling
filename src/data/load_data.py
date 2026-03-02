import pandas as pd

def load_nvda(path="data/raw/NVDA.csv"):
    return pd.read_csv(path)