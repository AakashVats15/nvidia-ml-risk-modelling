from src.pipelines.risk_pipeline import run_risk_pipeline
from src.pipelines.forecasting_pipeline import run_forecasting_pipeline

def test_risk_pipeline():
    df, vol, v, cv, dd = run_risk_pipeline()
    assert df is not None

def test_forecasting_pipeline():
    df, m, preds = run_forecasting_pipeline()
    assert df is not None