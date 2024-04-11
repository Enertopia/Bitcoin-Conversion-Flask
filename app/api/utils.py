import requests

def get_exchange_rate(currency_from, currency_to):
    response = requests.get(f"https://api.exchangeratesapi.io/latest?base={currency_from}&symbols={currency_to}")
    data = response.json()
    return data['rates'][currency_to]
