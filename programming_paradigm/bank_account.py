# bank_account.py

class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)
        print(f"Deposited: ${float(amount):.2f}")  # Dollar + 2 decimals

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            print("Insufficient funds.")  # Ends with period
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")  # Dollar + 2 decimals

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")  # Dollar + 2 decimals
