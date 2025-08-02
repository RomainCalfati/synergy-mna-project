
import pandas as pd

def load_synergy_benchmarks(file_path="mna_deals.xlsx"):
    df = pd.read_excel(file_path)

    # Calcul des médianes
    benchmarks = {
        "cost_synergy_pct": df["Cost Synergy %"].median() / 100,
        "revenue_synergy_pct": df["Revenue Synergy %"].median() / 100,
        "synergy_ebit_margin": df["EBIT Margin %"].median() / 100,
        "integration_cost": df["Integration Cost ($M)"].median(),
        "duration_years": int(df["Duration (years)"].median())
    }

    return benchmarks
