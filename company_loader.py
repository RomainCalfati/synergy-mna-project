
import yfinance as yf

def get_company_data(ticker, default_wacc=0.08):
    stock = yf.Ticker(ticker)
    info = stock.info

    try:
        name = info['longName']
        revenue = info['totalRevenue'] / 1e6
        ebitda = info['ebitda'] / 1e6
        shares_outstanding = info['sharesOutstanding'] / 1e6

        ebitda_margin = ebitda / revenue
        wacc = default_wacc

        return {
            "name": name,
            "revenue": round(revenue, 2),
            "ebitda": round(ebitda, 2),
            "ebitda_margin": round(ebitda_margin, 4),
            "wacc": round(wacc, 4),
            "shares_outstanding": round(shares_outstanding, 2)
        }

    except Exception as e:
        print(f"Erreur de récupération des données pour {ticker} : {e}")
        return None
