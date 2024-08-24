import csv
from banck_account import BankAccont
from typing import Dict
import os

class CsvHelper():
    def __init__(self, csv_path) -> None:
        self.csv_path = csv_path

    def save_to_csv(self, accounts:Dict[str, BankAccont]):
        with open(self.csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Balance'])
            for account in accounts.values():
                writer.writerow([account.name, account.balance])

    def load_from_csv(self):
        accounts:Dict[str, BankAccont] = dict()
        if os.path.exists(self.csv_path):
            with open(self.csv_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['Name']
                    balance = float(row['Balance'])
                    accounts[name] = BankAccont(name, balance)
        return accounts