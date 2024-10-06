class BankAccount:
    def __init__(self, Account_balance = 0):
        self.Account_balance = Account_balance
    def deposit(self, amount):
           self.Account_balance += amount
    def withdraw(self, amount):
           if amount > 0 and self.Account_balance >= amount:
                self.Account_balance -= amount
                return True
           elif amount > self.Account_balance:
                return False              
    def display_balance(self):
        print(f"Current Balance: ${self.Account_balance}")
