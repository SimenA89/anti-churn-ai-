from agents.analyzer_agent import AnalyzerAgent
from agents.engagement_agent import EngagementAgent
from agents.loyalty_agent import LoyaltyAgent
from agents.feedback_agent import FeedbackAgent
from utils.data_loader import load_customer_data

def main():
    # Last kundedata
    customers = load_customer_data()

    # Initialiser agenter
    analyzer = AnalyzerAgent()
    engagement = EngagementAgent()
    loyalty = LoyaltyAgent()
    feedback = FeedbackAgent()

    # Analyser kunder og iverksett tiltak
    risk_customers = analyzer.identify_risk_customers(customers)
    
    for customer in risk_customers:
        print(f"\nHåndterer risikokunde: {customer['name']}")
        
        # Engasjement
        message = engagement.generate_message(customer)
        print(f"Engasjements-melding: {message}")
        
        # Lojalitetstilbud
        offer = loyalty.generate_offer(customer)
        print(f"Lojalitetstilbud: {offer}")
        
        # Tilbakemelding
        feedback_request = feedback.request_feedback(customer)
        print(f"Tilbakemeldingsforespørsel: {feedback_request}")

if __name__ == "__main__":
    main()
