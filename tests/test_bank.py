import tempfile
import unittest
from pathlib import Path

from banking.repository import AccountRepository
from banking.service import BankService


class BankServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        file_path = str(Path(self.temp_dir.name) / "accounts.json")
        self.bank = BankService(AccountRepository(file_path))

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_account(self):
        account = self.bank.create_account("Ashok", 1000)
        self.assertEqual(account.holder_name, "Ashok")
        self.assertEqual(account.balance, 1000)
        self.assertTrue(account.account_number)

    def test_deposit(self):
        account = self.bank.create_account("Ashok", 100)
        updated = self.bank.deposit(account.account_number, 50)
        self.assertEqual(updated.balance, 150)

    def test_withdraw(self):
        account = self.bank.create_account("Ashok", 100)
        updated = self.bank.withdraw(account.account_number, 40)
        self.assertEqual(updated.balance, 60)

    def test_insufficient_balance(self):
        account = self.bank.create_account("Ashok", 100)
        with self.assertRaises(ValueError):
            self.bank.withdraw(account.account_number, 101)

    def test_transaction_history(self):
        account = self.bank.create_account("Ashok", 100)
        self.bank.deposit(account.account_number, 50)
        history = self.bank.transaction_history(account.account_number)
        self.assertEqual(len(history), 2)
        self.assertEqual(history[-1].transaction_type, "DEPOSIT")

    def test_reject_zero_deposit(self):
        account = self.bank.create_account("Ashok", 100)
        with self.assertRaises(ValueError):
            self.bank.deposit(account.account_number, 0)


if __name__ == "__main__":
    unittest.main()
