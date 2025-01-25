class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance= initial_balance

    def deposit(self, amount: float):
        self.account_balance += amount
       

       

    def withdraw(self, amount):
        if amount<=0:
            raise Exception("amount has to be positive and not 0")
        
        elif amount>0:
            self.account_balance-= amount
        

        else:
            print("insufficient funds")
           
    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")