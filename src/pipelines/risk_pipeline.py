import pandas as pd
from src.data.load_data import load_nvda
from src.data.preprocess import preprocess
from src.risk.volatility_models import realized_vol
from src.risk.var_cvar import var, cvar
from src.risk.drawdowns import drawdowns

def run_risk_pipeline(path="data/raw/NVDA.csv"):
    df = load_nvda(path)
    df = preprocess(df)
    vol = realized_vol(df)
    v = var(df)
    cv = cvar(df)
    dd = drawdowns(df)
    return df, vol, v, cv, dd