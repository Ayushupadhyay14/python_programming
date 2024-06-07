""" create Account class with 2 attributes balance
account no create methis for debit credit printting the balnce """
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Total balance =", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total balance =", self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
#print("Your account balance is:", acc1.balance)
#print("Your account number is:", acc1.acc_no)
    