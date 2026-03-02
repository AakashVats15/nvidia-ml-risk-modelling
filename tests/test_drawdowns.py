import pandas as pd
from src.risk.drawdowns import drawdowns

def test_drawdowns():
    df = pd.DataFrame({"Return": [0.01, -0.02, 0.03]})
    dd = drawdowns(df)
    assert len(dd) == 3