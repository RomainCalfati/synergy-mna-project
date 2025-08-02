
class Company:
    def __init__(self, name, revenue, ebitda, ebit_margin, wacc, shares_outstanding):
        self.name = name
        self.revenue = revenue
        self.ebitda = ebitda
        self.ebit_margin = ebit_margin
        self.wacc = wacc
        self.shares_outstanding = shares_outstanding

    def __repr__(self):
        return (f"{self.name} - Revenue: {self.revenue}M, EBITDA: {self.ebitda}M, "
                f"EBITDA Margin: {self.ebit_margin*100:.1f}%, WACC: {self.wacc*100:.1f}%, "
                f"Shares: {self.shares_outstanding}M")
