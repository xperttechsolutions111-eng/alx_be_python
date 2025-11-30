class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        self.balance += amount
        print(f"Deposited: ${amount:.1f}")  # ONLY ONE print

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
