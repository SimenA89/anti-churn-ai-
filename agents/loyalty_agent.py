class LoyaltyAgent:
    def generate_offer(self, customer):
        if customer['product'] == 'Bilforsikring':
            return f"Vi vil gjerne tilby deg 10% rabatt på din {customer['product']} og 6 måneder gratis veihjelp!"
        return f"Vi vil gjerne tilby deg 15% rabatt på din {customer['product']} for neste år!"
