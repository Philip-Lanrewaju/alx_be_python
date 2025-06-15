# bank_account.py

class BankAccount:
    """A simple bank account class with deposit, withdraw, and balance functionality."""
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount from account balance if sufficient funds exist."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Displays the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
