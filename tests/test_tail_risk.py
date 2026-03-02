import pandas as pd
from src.risk.tail_risk import tail_ratio

def test_tail_ratio():
    df = pd.DataFrame({"Return": [-0.02, 0.03, -0.01, 0.04]})
    r = tail_ratio(df)
    assert r != 0