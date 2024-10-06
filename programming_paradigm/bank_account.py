class BankAccount:
    def __init__(self, Account_balance = 0):
        self.Account_balance = Account_balance
    def deposit(self, amount):
        self.Account_balance += amount
        print(f"Deposit: {amount}")
    def withdraw(self, amount):
        self.Account_balance-= amount
        if amount <= self.Account_balance:
            print(f"Withdraw: {amount}")
        else:
            print("Insufficient funds.")
    def display_balance(self):
        print(f"Current Balance: {self.Account_balance}")
obj= BankAccount(100)
obj.deposit(40)
obj.withdraw(50)