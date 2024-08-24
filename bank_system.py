from banck_account import BankAccont
from csv_helper import CsvHelper
import threading
import atexit

class BankingSystem:
    def __init__(self, csv_file='accounts.csv'):
        self.accounts = dict()
        self.csv_file = csv_file
        self.csv_helper = CsvHelper(self.csv_file)
        self.lock = threading.Lock()  # Lock for the overall banking system
        self.load_accounts()
        atexit.register(self.save_accounts)
    
    def create_account(self, name, initial_balance=0):
        with self.lock:
            if name in self.accounts:
                raise ValueError("Account with this name already exists")
            self.accounts[name] = BankAccont(name, initial_balance)
    
    def get_account(self, name):
        with self.lock:
            if name not in self.accounts:
                raise ValueError("Account does not exist")
            return self.accounts[name]
    
    def deposit(self, name, amount):
        account = self.get_account(name)
        with account.lock:
            if amount > 0:
                account.balance += amount
    
    def withdraw(self, name, amount):
        account = self.get_account(name)
        with account.lock:
            if 0 < amount <= account.balance:
                account.balance -= amount
            else:
                raise ValueError("Insufficient funds")
    
    def transfer(self, from_name, to_name, amount):
        from_account = self.get_account(from_name)
        to_account = self.get_account(to_name)
        
        # Lock accounts in a consistent order to prevent deadlock
        first, second = sorted([from_account, to_account], key=lambda acc: acc.name)
        with first.lock, second.lock:
            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
            else:
                raise ValueError("Insufficient funds")
    
    def save_accounts(self):
        with self.lock:
            self.csv_helper.save_to_csv(self.accounts)
    
    def load_accounts(self):
        with self.lock:
            self.accounts = self.csv_helper.load_from_csv()