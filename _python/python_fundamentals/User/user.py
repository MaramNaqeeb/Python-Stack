class user:
    def __init__ (self,name,email_address):
        self.name=name
        self.email=email_address
        self.account_balance=0
      

    def make_deposit (self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self
    def transfer(self, other_user, amount):
        other_user.account_balance += amount 
        self.account_balance -= amount
        return self

saeed= user("saeed","saeed12@gmail.com").make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(500).display_user_balance()

Hasan= user("Hasan","Hasan44@gmail.com")
Hasan.make_deposit(2000).make_deposit(2000).make_withdrawal(800).make_withdrawal(800).display_user_balance()

Maram= user("Maram","maramnaqib1998@gmail.com").make_deposit(4000).make_withdrawal(2000).make_withdrawal(2000).make_withdrawal(2000).display_user_balance()

saeed.transfer(Maram,500)
saeed.display_user_balance()
Maram.display_user_balance()













