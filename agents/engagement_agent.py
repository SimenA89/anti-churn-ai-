class EngagementAgent:
    def generate_message(self, customer):
        return f"Hei {customer['name']}, vi ser at du har vært kunde hos oss i {customer['years_with_bank']} år. Vi setter stor pris på deg og lurer på om det er noe vi kan hjelpe deg med?"
