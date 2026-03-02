from src.pipelines.risk_pipeline import run_risk_pipeline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import datetime
import os

def main():
    df, vol, v, cv, dd = run_risk_pipeline()

    ts = datetime.datetime.now().strftime("%Y-%m-%d")
    out_dir = r"E:\Personal\GitHub\Python Code Repo\nvidia-ml-risk-modelling\scripts\Risk Report"
    os.makedirs(out_dir, exist_ok=True)
    pdf_path = os.path.join(out_dir, f"risk_report_{ts}.pdf")

    with PdfPages(pdf_path) as pdf:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df["Return"], label="Returns")
        ax.axhline(v, color="red", label="VaR")
        ax.axhline(cv, color="orange", label="CVaR")
        ax.set_title("Returns, VaR, CVaR")
        ax.set_ylabel("Return")
        ax.legend()
        pdf.savefig(fig)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(vol, label="Realized Volatility")
        ax.set_title("Volatility")
        ax.set_ylabel("Volatility")
        ax.legend()
        pdf.savefig(fig)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(dd, label="Drawdowns")
        ax.set_title("Drawdowns")
        ax.set_ylabel("Drawdown")
        ax.set_xlabel("Time")
        ax.legend()
        pdf.savefig(fig)
        plt.close(fig)

        d = {
            "VaR": [v],
            "CVaR": [cv],
            "Volatility Mean": [vol.mean()],
            "Max Drawdown": [dd.min()]
        }
        summary = pd.DataFrame(d)

        fig, ax = plt.subplots(figsize=(6, 1))
        ax.axis("off")
        ax.table(cellText=summary.values, colLabels=summary.columns, loc="center")
        pdf.savefig(fig)
        plt.close(fig)

if __name__ == "__main__":
    main()