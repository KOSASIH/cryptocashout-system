import unittest
from atm_software.atm_ui import ATMUI
from atm_software.atm_business_logic import ATMBusinessLogic
from atm_software.atm_communication import ATMCommunication

class TestATMSoftwareIntegration(unittest.TestCase):
    def test_atm_workflow(self):
        # Set up the ATM software components
        ui = ATMUI()
        bl = ATMBusinessLogic()
        comm = ATMCommunication()

        # Simulate a user interaction
        user_input = "1"  # Select an option
        ui.display_menu()
        selected_option = ui.get_user_input("Enter an option: ")
        self.assertEqual(selected_option, user_input)

        # Process the transaction
        transaction = {"amount": 10, "currency": "BTC"}
        bl.process_transaction(transaction)
        comm.send_transaction_to_backend(transaction)

        # Verify that the transaction is processed correctly
        self.assertTrue(True)  # Replace with actual verification logic

    def test_atm_error_handling(self):
        # Set up the ATM software components
        ui = ATMUI()
        bl = ATMBusinessLogic()
        comm = ATMCommunication()

        # Simulate a user interaction with an invalid input
        user_input = "abc"  # Invalid input
        ui.display_menu()
        selected_option = ui.get_user_input("Enter an option: ")
        self.assertRaises(ValueError, bl.validate_user_input, selected_option)

        # Verify that the error is handled correctly
        self.assertTrue(True)  # Replace with actual verification logic

if __name__ == "__main__":
    unittest.main()
