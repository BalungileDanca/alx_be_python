class BankAccount:
    def __init__(self, Account_balance):
        self.Account_balance = Account_balance
        
    def deposit(self):
        Amount = float(input("Amount you want to deposit: "))
        Amount += self.Account_balance
        print(f"Deposit: {Amount}")
    def withdraw(self):
        Amount = float(input("Amount you want to withdraw: "))
        Amount -= self.Account_balance

        if Amount <= self.Account_balance:
            print(f"withdraw: {Amount}")
        else:
            print("Insufficient funds.")
    def display_balance(self):
        print(f"Current balance: {self.Account_balance}")
obj = BankAccount(100)
obj.deposit()
obj.withdraw()
obj.display_balance()
