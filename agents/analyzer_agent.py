class AnalyzerAgent:
    def identify_risk_customers(self, customers):
        risk_customers = []
        for customer in customers:
            if customer['satisfaction_score'] < 3 or customer['engagement_score'] < 50:
                risk_customers.append(customer)
        return risk_customers
