class BankAccount:
    def __init__ (self,int_rate=.01, balance=0):
        self.int_rate=int_rate
        self.account_balance= balance

    def deposit(self, amount):
        self.account_balance += amount
        return self
		
    def withdraw(self, amount):
        if amount<=self.account_balance:
            self.account_balance -= amount
        else:
            self.account_balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
      print(self.account_balance)
      return self

        
    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        return self

account1 = BankAccount(int_rate=.01, balance=600)
account1.deposit(200).deposit(30).deposit(80).withdraw(500).yield_interest().display_account_info()

account2 = BankAccount(int_rate=.01, balance=1000)
account1.deposit(100).deposit(300).deposit(70).withdraw(700).yield_interest().display_account_info()
