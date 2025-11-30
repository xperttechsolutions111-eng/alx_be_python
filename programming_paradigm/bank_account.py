# bank_account.py

class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        # Deposit message: ONE decimal place
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            # Insufficient funds: print exactly once, ends with period
            print("Insufficient funds.")
        else:
            self.balance -= amount
            # Withdraw message: ONE decimal place
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        # Display balance: TWO decimal places
        print(f"Current Balance: ${self.balance:.2f}")
