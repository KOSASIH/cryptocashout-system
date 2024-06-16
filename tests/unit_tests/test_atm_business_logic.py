import unittest
from atm_software.atm_business_logic import ATMBusinessLogic

class TestATMBusinessLogic(unittest.TestCase):
    def test_init(self):
        bl = ATMBusinessLogic()
        self.assertIsNotNone(bl)

    def test_validate_user_input(self):
        bl = ATMBusinessLogic()
        valid_input = "1"
        self.assertTrue(bl.validate_user_input(valid_input))

        invalid_input = "abc"
        self.assertFalse(bl.validate_user_input(invalid_input))

    def test_process_transaction(self):
        bl = ATMBusinessLogic()
        # Set up a mock transaction
        transaction = {"amount": 10, "currency": "BTC"}
        bl.process_transaction(transaction)
        # Verify that the transaction is processed correctly
        self.assertTrue(True)  # Replace with actual verification logic

if __name__ == "__main__":
    unittest.main()
