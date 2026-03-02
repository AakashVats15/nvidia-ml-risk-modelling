from src.pipelines.risk_pipeline import run_risk_pipeline
import matplotlib.pyplot as plt

def main():
    df, vol, v, cv, dd = run_risk_pipeline()

    fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

    axs[0].plot(df["Return"], label="Returns")
    axs[0].axhline(v, color="red", label="VaR")
    axs[0].axhline(cv, color="orange", label="CVaR")
    axs[0].set_ylabel("Return")
    axs[0].legend()

    axs[1].plot(vol, label="Realized Volatility")
    axs[1].set_ylabel("Volatility")
    axs[1].legend()

    axs[2].plot(dd, label="Drawdowns")
    axs[2].set_ylabel("Drawdown")
    axs[2].set_xlabel("Time")
    axs[2].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
