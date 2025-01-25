class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance= initial_balance

    def deposit(self, amount: float):
        self.account_balance += amount
       

       

    def withdraw(self, amount):
        if self.account_balance>= amount:
            self.account_balance-= amount
            return True
        
        return False
        

      
           
    def display_balance(self:float):
        print(f"Current Balance: ${self.account_balance}")