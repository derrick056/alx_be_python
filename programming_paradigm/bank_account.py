class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance= initial_balance

    def deposit(self, amount):
        if amount>0:
            self.account_balance+= amount
            print(f"the amount {amount} has been deposited and your new balance is {self.account_balance}")

        else:
            print("amount has to be positive and not 0")

    def withdraw(self, amount):
        if amount<=0:
            raise Exception("amount has to be positive and not 0")
        elif amount> self.account_balance:
            print("insufficient funds")

        else:
            self.account_balance-= amount
            print(f"the amount {amount} has been withdrawn and your new balance is {self.account_balance}")

    def display_balance(self):
        print(f"you account balance is {self.account_balance}")