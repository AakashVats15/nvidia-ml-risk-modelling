import pandas as pd

def predict_risk(model, df: pd.DataFrame):
    X = df[["Return"]]
    return model.predict(X)