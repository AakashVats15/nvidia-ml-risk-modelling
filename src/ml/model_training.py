import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def train_model(df: pd.DataFrame):
    X = df[["Return"]]
    y = df["Return"].shift(-1).dropna()
    X = X.iloc[:-1]
    m = RandomForestRegressor()
    m.fit(X, y)
    return m