import pandas as pd
import numpy as np

def bootstrap_scenarios(df: pd.DataFrame, n=1000):
    return np.random.choice(df["Return"], size=n, replace=True)