class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance= initial_balance

    def deposit(self, amount: float):
        self.account_balance += amount
        print(f"Deposited: ${amount}")

       

    def withdraw(self, amount):
        if amount<=0:
            raise Exception("amount has to be positive and not 0")
        elif amount> self.account_balance:
            print("insufficient funds")

        else:
            self.account_balance-= amount
            print(f"Withdrew: ${amount}")
    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")