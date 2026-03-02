import pandas as pd
from src.risk.volatility_models import realized_vol

def test_realized_vol():
    df = pd.DataFrame({"Return": [0.01, -0.02, 0.03]})
    v = realized_vol(df, window=2)
    assert len(v) == 3