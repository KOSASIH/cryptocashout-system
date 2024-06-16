class FiatCurrencyConverter:
    def __init__(self):
        self.exchange_rate = 1.0  # Initialize exchange rate

    def convert_pi_coin_to_fiat(self, amount):
        return amount * self.exchange_rate
