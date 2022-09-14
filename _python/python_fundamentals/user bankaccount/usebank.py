class BankAccount:
    def __init__ (self,int_rate=.01, balance=0):
        self.int_rate=int_rate
        self.account_balance= balance

    def deposit(self, amount):
        self.account_balance += amount
        return self
		
    def withdraw(self, amount):
        if (amount<=self.account_balance):
            self.account_balance -= amount
        else:
            self.account_balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
      self.account_balance=(2000)
      return self

        
    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        return self

class user:
    def __init__ (self,name,email):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate=0.02,balance=0)
        
    def make_deposit (self,amount):
        self.account.deposit(amount)
        
    def make_withdraw (self,amount):
        self.account.withdraw(amount)
    
        
    def display_user_balance (self):
        self.account.display_account_info()
  




