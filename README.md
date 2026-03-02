# **NVIDIA ML Risk Modelling**

A modular, hedge‑fund‑style research engine for **single‑stock risk analysis**, **volatility modelling**, **tail‑risk estimation**, and **ML‑based forecasting**.  
Built with a clean, production‑aligned architecture and minimalistic quant‑research conventions.

---

## **📁 Project Structure**

```
nvidia-ml-risk-modelling/
│
├── config/
│   ├── paths.py
│   ├── model_config.py
│   └── risk_config.py
│
├── scripts/
│   ├── Risk Report/
│   ├── risk_visualization.py
│   └── risk_report.py
│
├── src/
│   ├── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   ├── load_data.py
│   │   └── preprocess.py
│   │
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── model_training.py
│   │   ├── model_selection.py
│   │   └── risk_prediction.py
│   │
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── risk_pipeline.py
│   │   └── forecasting_pipeline.py
│   │
│   ├── risk/
│   │   ├── __init__.py
│   │   ├── volatility_models.py
│   │   ├── var_cvar.py
│   │   ├── tail_risk.py
│   │   ├── drawdowns.py
│   │   └── scenario_generation.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logging_utils.py
│       ├── plotting.py
│       └── metrics.py
│
├── tests/
│   ├── test_volatility.py
│   ├── test_var_cvar.py
│   ├── test_tail_risk.py
│   ├── test_drawdowns.py
│   └── test_pipelines.py
│
├── data/
│   ├── raw/
│   │   └── NVDA.csv
│   └── processed/
│
├── setup.py
├── requirements.txt
└── README.md
```

---

## **📌 Features**

### **Risk Modelling**
- Realized volatility  
- Historical VaR & CVaR  
- Tail‑risk ratio  
- Drawdown curves  
- Scenario generation (bootstrap)

### **Machine Learning**
- Minimal forecasting model (Random Forest)  
- Time‑series cross‑validation  
- Risk prediction pipeline

### **Pipelines**
- End‑to‑end risk pipeline  
- End‑to‑end forecasting pipeline  

### **Visualization**
- Combined risk dashboard  
- PDF risk report generator  
- Time‑aligned multi‑panel charts

---

## **📄 Generating a Risk Report**

Run:

```
python scripts/risk_report.py
```

A PDF will be saved to:

```
scripts/Risk Report/
```

---

## **📊 Visualizing Risk Metrics**

Run:

```
python scripts/risk_visualization.py
```

This displays:

- Returns + VaR + CVaR  
- Realized volatility  
- Drawdowns  

---

## **🧪 Running Tests**

From project root:

```
pytest
```

or a specific file:

```
pytest tests/test_pipelines.py
```

---

## **⚙ Installation**

Install the package in editable mode:

```
pip install -e .
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## **📈 Data Requirements**

Place your raw NVDA data here:

```
data/raw/NVDA.csv
```

The preprocessing pipeline will handle returns and formatting.

---

## **🎯 Purpose**

This repository is designed to mirror the structure and discipline of real quant research teams:

- modular  
- testable  
- pipeline‑driven  
- minimalistic  
- production‑aligned  

It serves as a foundation for expanding into:

- factor modelling  
- ML‑driven risk forecasting  
- portfolio analytics  
- systematic strategy research
