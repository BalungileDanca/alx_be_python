class BankAccount:
    def __init__(self, Account_balance = 0):
        self.Account_balance = Account_balance
        
    def deposit(self, Amount):
        Amount = float(input("Amount you want to deposit: "))
        self.Account_balance += Amount
        print(f"Deposit: {Amount}")
    def withdraw(self, Amount):
        self.Amount = float(input("Amount you want to withdraw: "))
        self.Account_balance -= Amount

        if self.Account_balance >= Amount:
            print(f"withdraw: {Amount}")
        else:
            print("Insufficient funds.")
    def display_balance(self):
        print(f"Current balance: {self.Account_balance}")
