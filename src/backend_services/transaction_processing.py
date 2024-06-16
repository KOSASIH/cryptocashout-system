class TransactionProcessing:
    def __init__(self):
        self.transactions = []

    def process_transaction(self, transaction):
        # Process transaction logic
        self.transactions.append(transaction)
        print(f"Transaction processed: {transaction}")
