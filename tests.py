import unittest
from bank_system import BankingSystem
import threading

class TestBankingSystem(unittest.TestCase):
    
    def setUp(self):
        self.bank = BankingSystem(csv_file='test_accounts.csv')
        self.bank.create_account('Alice', 100)
        self.bank.create_account('Bob', 50)
    
    def tearDown(self):
        import os
        if os.path.exists('test_accounts.csv'):
            os.remove('test_accounts.csv')
    
    def test_deposit(self):
        self.bank.deposit('Alice', 50)
        alice = self.bank.get_account('Alice')
        self.assertEqual(alice.balance, 150)
    
    def test_withdraw(self):
        self.bank.withdraw('Alice', 30)
        alice = self.bank.get_account('Alice')
        self.assertEqual(alice.balance, 70)
    
    def test_overdraft(self):
        with self.assertRaises(ValueError):
            self.bank.withdraw('Alice', 200)
    
    def test_transfer(self):
        self.bank.transfer('Alice', 'Bob', 30)
        alice = self.bank.get_account('Alice')
        bob = self.bank.get_account('Bob')
        self.assertEqual(alice.balance, 70)
        self.assertEqual(bob.balance, 80)
    
    def test_concurrent_transfer(self):
        def transfer_amount():
            for _ in range(1000):
                self.bank.transfer('Alice', 'Bob', 1)
                self.bank.transfer('Bob', 'Alice', 1)
        
        threads = [threading.Thread(target=transfer_amount) for _ in range(10)]
        
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
        
        alice = self.bank.get_account('Alice')
        bob = self.bank.get_account('Bob')
        self.assertEqual(alice.balance, 100)
        self.assertEqual(bob.balance, 50)

    def test_save_and_load(self):
        self.bank.save_accounts()
        new_bank = BankingSystem(csv_file='test_accounts.csv')
        alice = new_bank.get_account('Alice')
        self.assertEqual(alice.balance, 100)

if __name__ == '__main__':
    unittest.main()