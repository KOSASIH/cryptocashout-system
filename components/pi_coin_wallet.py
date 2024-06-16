class PiCoinWallet:
    def __init__(self):
        self.pi_coin_balance = 0

    def add_pi_coin(self, amount):
        self.pi_coin_balance += amount

    def get_pi_coin_balance(self):
        return self.pi_coin_balance
