import requests

class FiatExchangeRateAPI:
    def __init__(self):
        self.api_url = "https://api.exchange_rate.com/latest"

    def get_exchange_rate(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()["exchange_rate"]
        return None
