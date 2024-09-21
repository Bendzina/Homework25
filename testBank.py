import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(1000)

    def test_initial_balance(self):
        
        self.assertEqual(self.account.balance, 1000)

    def test_deposit(self):
       
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw_success(self):
        
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1100)

    def test_negative_deposit(self):
       
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

if __name__ == '__main__':
    unittest.main()
