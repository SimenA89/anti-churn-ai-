import json

def load_customer_data():
    with open('data/customer_data.json', 'r') as file:
        return json.load(file)
