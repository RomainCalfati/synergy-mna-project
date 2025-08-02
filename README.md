# M&A Synergy Calculator 🔍📊

This project is a **Python-based financial tool** designed to estimate the value creation potential of mergers and acquisitions (M&A) by modeling cost and revenue synergies, integration costs, and projected timeframes. It automates the synergy calculation process, offering analytical support that mirrors real M&A modeling practices used in investment banking.

## ⚙️ Features

- **Automated synergy calculation** based on benchmarked % assumptions.
- **Excel integration**: users can input their own set of comparable transactions.
- **Monte Carlo-inspired output range** to reflect uncertainty in real-life deals.
- **Modular structure** for easy adaptation to new deal types or sectors.
- **Company data retrieval** via `yfinance` or user entry.

## 📂 Structure

- `main.ipynb`: Jupyter Notebook where the full simulation is run.
- `company.py`: Stores company object structure (revenue, EBITDA, margin, etc.).
- `synergy_model.py`: Core financial model computing value creation from synergies.
- `synergy_loader.py`: Loads historical M&A benchmarks from an Excel sheet.
- `mna_deals.xlsx`: Example file containing past transactions for benchmarking.

## 🔧 How to Use

1. Clone the repository
2. Add your own `mna_deals.xlsx` in the project folder (or use the sample one which is an example of railway industry transactions in the context of the potential Union Pacific - Norfolk Southern M&A deal)
3. Launch `main.ipynb` in Jupyter
4. Input tickers to get the data of each company
5. Run and interpret the results
