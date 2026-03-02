import pandas as pd

def drawdowns(df: pd.DataFrame):
    cum = (1 + df["Return"]).cumprod()
    peak = cum.cummax()
    dd = (cum - peak) / peak
    return dd