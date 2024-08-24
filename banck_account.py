import threading

class BankAccont:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()  # Lock for this account

    def __str__(self):
        return f'{self.name},{self.balance}'