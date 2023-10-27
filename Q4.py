""""
Q4. Write a Python program to create a class named BankAccount with attributes
    owner and balance. Implement methods to deposit, withdraw, and check the 
    balance of the account. Also, implement a method to transfer money from 
    one account to another."""


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Rs. {amount} Deposited\nAccount Balance: {self.balance}"
        else:
            raise ValueError("Invalid Amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Rs. {amount} Withdrew\nAccount Balance: {self.balance}"
        else:
            raise ValueError("Invalid Amount or Insufficient Balance")

    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            return f"Rs. {amount} Transferred from {self.owner} to {other_account.owner}\nAccount Balance: {self.balance}"
        else:
            raise ValueError("Invalid Amount or Insufficient Balance")

    def check_balance(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"

ac1 = BankAccount("A", 2000)
ac2 = BankAccount("B", 8000)

try:
    print(f"{ac1.transfer(ac2, 1000)}\nA/C 1: {ac1.balance}\nA/C 2: {ac2.balance}")
except ValueError as e:
    print(e)
