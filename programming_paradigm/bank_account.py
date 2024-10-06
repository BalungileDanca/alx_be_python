class BankAccount:
    def __init__(self, Account_balance = 0):
        self.__Account_balance = Account_balance
    def deposit(self, amount):
           self.__Account_balance += amount
    def withdraw(self, amount):
           if amount > 0 and self.__Account_balance >= amount:
                self.__Account_balance -= amount
                return True
           elif amount > self.__Account_balance:
                return False              
    def display_balance(self):
        print(f"Current Balance: ${float(self.__Account_balance)}")
