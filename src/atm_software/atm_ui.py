import tkinter as tk
from atm_business_logic import ATMBusinessLogic

class ATMUI:
    def __init__(self, master):
        self.master = master
        self.master.title("CryptoCashOut ATM")
        self.business_logic = ATMBusinessLogic()

        # Create UI components
        self.balance_label = tk.Label(master, text="Balance: ")
        self.balance_label.pack()

        self.withdraw_button = tk.Button(master, text="Withdraw", command=self.withdraw_fiat)
        self.withdraw_button.pack()

        self.deposit_button = tk.Button(master, text="Deposit", command=self.deposit_pi_coin)
        self.deposit_button.pack()

    def withdraw_fiat(self):
        amount = self.business_logic.get_withdrawal_amount()
        self.business_logic.withdraw_fiat(amount)

    def deposit_pi_coin(self):
        amount = self.business_logic.get_deposit_amount()
        self.business_logic.deposit_pi_coin(amount)
