class BankAccount:
    def __init__(self, Account_balance):
        self.Account_balance = Account_balance
    def deposit(self):
        amount = float(input("Enter the amount you want to Deposit: "))
        amount += self.Account_balance
        print(f"Deposit: {amount}")
    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw: "))
        amount -= self.Account_balance
        if amount <= self.Account_balance:
            print(f"Withdraw: {amount}")
        else:
            print("Insufficient funds.")
    def display_balance(self):
        print(f"Current Balance: {self.Account_balance}")

obj = BankAccount(20)
obj.deposit()
obj.withdraw()
