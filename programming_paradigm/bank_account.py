class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Error: Insufficient funds"
        if amount <= 0:
            return "Withdrawal amount must be positive"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

    def display_balance(self):
        return f"{self.account_name} balance: {self.balance}"