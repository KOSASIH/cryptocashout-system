import pi_coin_wallet
from fiat_currency_converter import FiatCurrencyConverter

class ATMBusinessLogic:
    def __init__(self):
        self.pi_coin_wallet = pi_coin_wallet.PiCoinWallet()
        self.fiat_currency_converter = FiatCurrencyConverter()

    def get_withdrawal_amount(self):
        # Get user input for withdrawal amount
        amount = input("Enter withdrawal amount: ")
        return amount

    def withdraw_fiat(self, amount):
        # Convert Pi Coin to fiat currency
        fiat_amount = self.fiat_currency_converter.convert_pi_coin_to_fiat(amount)
        # Dispense fiat currency
        print(f"Dispensing {fiat_amount} fiat currency")

    def get_deposit_amount(self):
        # Get user input for deposit amount
        amount = input("Enter deposit amount: ")
        return amount

    def deposit_pi_coin(self, amount):
        # Add Pi Coin to user's wallet
        self.pi_coin_wallet.add_pi_coin(amount)
        print(f"Deposited {amount} Pi Coin")
