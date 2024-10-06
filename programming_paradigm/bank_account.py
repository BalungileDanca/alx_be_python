class BankAccount:
    def __init__(self, Account_balance = 0):
        self.Account_balance = Account_balance
    def deposit(self, amount):
        if amount > 0:
           self.Account_balance += amount
           print(f"Deposit: ${amount}")
        else:
            print("The amount must be greater than zero")
    def withdraw(self, amount):
        if amount > 0:
            self.Account_balance-= amount
            print(f"Withdraw: ${amount}")
            return True
        elif amount > self.Account_balance:
            print("Insufficient funds.")
            return False
        else:
            print("amount must be greater than zero")      
    def display_balance(self):
        print(f"Current Balance: ${self.Account_balance}")
