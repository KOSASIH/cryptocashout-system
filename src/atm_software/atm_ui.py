import asyncio
import logging
import os
from typing import Dict, List

import aiohttp
import tkinter as tk
from tkinter import messagebox

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ATMUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ATM System")
        self.root.geometry("400x300")

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root, width=20)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, width=20, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        self.balance_label = tk.Label(self.root, text="Balance:")
        self.balance_label.pack()

        self.balance_value_label = tk.Label(self.root, text="")
        self.balance_value_label.pack()

        self.transaction_history_button = tk.Button(self.root, text="Transaction History", command=self.transaction_history)
        self.transaction_history_button.pack()

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        self.logout_button.pack()

    async def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Call backend API to authenticate user
        async with aiohttp.ClientSession() as session:
            async with session.post("https://backend.example.com/api/authenticate", json={"username": username, "password": password}) as response:
                if response.status == 200:
                    # Login successful, show balance and transaction history
                    self.balance_value_label.config(text="Balance: $1000.00")
                    self.transaction_history_button.config(state="normal")
                    self.withdraw_button.config(state="normal")
                    self.deposit_button.config(state="normal")
                    self.logout_button.config(state="normal")
                else:
                    messagebox.showerror("Error", "Invalid username or password")

    async def transaction_history(self):
        # Call backend API to get transaction history
        async with aiohttp.ClientSession() as session:
            async with session.get("https://backend.example.com/api/transaction_history") as response:
                if response.status == 200:
                    transaction_history = await response.json()
                    # Display transaction history
                    messagebox.showinfo("Transaction History", "\n".join([f"Date: {transaction['date']}, Amount: {transaction['amount']}" for transaction in transaction_history]))

    async def withdraw(self):
        # Call backend API to process withdrawal
        async with aiohttp.ClientSession() as session:
            async with session.post("https://backend.example.com/api/withdraw", json={"amount": 100}) as response:
                if response.status == 200:
                    # Withdrawal successful, update balance
                    self.balance_value_label.config(text="Balance: $900.00")
                else:
                    messagebox.showerror("Error", "Withdrawal failed")

    async def deposit(self):
        # Call backend API to process deposit
        async with aiohttp.ClientSession() as session:
            async with session.post("https://backend.example.com/api/deposit", json={"amount": 100}) as response:
                if response.status == 200:
                    # Deposit successful, update balance
                    self.balance_value_label.config(text="Balance: $1100.00")
                else:
                    messagebox.showerror("Error", "Deposit failed")

    async def logout(self):
        # Call backend API to logout
        async with aiohttp.ClientSession() as session:
            async with session.post("https://backend.example.com/api/logout") as response:
                if response.status == 200:
                    # Logout successful, reset UI
                    self.balance_value_label.config(text="")
                    self.transaction_history_button.config(state="disabled")
                    self.withdraw_button.config(state="disabled")
                    self.deposit_button.config(state="disabled")
                    self.logout_button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    atm_ui = ATMUI()
    atm_ui.run()
