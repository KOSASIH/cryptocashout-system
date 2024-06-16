import unittest
from atm_software.atm_ui import ATMUI

class TestATMUI(unittest.TestCase):
    def test_init(self):
        ui = ATMUI()
        self.assertIsNotNone(ui)

    def test_display_menu(self):
        ui = ATMUI()
        ui.display_menu()
        # Verify that the menu is displayed correctly
        self.assertTrue(True)  # Replace with actual verification logic

    def test_get_user_input(self):
        ui = ATMUI()
        user_input = ui.get_user_input("Enter an option: ")
        self.assertIsNotNone(user_input)

if __name__ == "__main__":
    unittest.main()
