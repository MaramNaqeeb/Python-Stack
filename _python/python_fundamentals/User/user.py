class user:
    def __init__ (self,name,email_address):
        self.name=name
        self.email=email_address
        self.account_balance=0

    def make_deposit (self,amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer(self, other_user, amount):
        other_user.account_balance += amount 
        self.account_balance -= amount

saeed= user("saeed","saeed12@gmail.com")
saeed.make_deposit(1000)
saeed.make_deposit(1000)
saeed.make_deposit(1000)
saeed.make_withdrawal(500)
saeed.display_user_balance()

Hasan= user("Hasan","Hasan44@gmail.com")
Hasan.make_deposit(2000)
Hasan.make_deposit(2000)
Hasan.make_withdrawal(800)
Hasan.make_withdrawal(800)
Hasan.display_user_balance()

Maram= user("Maram","maramnaqib1998@gmail.com")
Maram.make_deposit(4000)
Maram.make_withdrawal(2000)
Maram.make_withdrawal(2000)
Maram.make_withdrawal(2000)
Maram.display_user_balance()

saeed.transfer(Maram,500)
saeed.display_user_balance()
Maram.display_user_balance()













