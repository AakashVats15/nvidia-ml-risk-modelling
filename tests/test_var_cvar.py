import pandas as pd
from src.risk.var_cvar import var, cvar

def test_var_cvar():
    df = pd.DataFrame({"Return": [-0.05, 0.02, -0.01]})
    assert var(df) is not None
    assert cvar(df) is not None