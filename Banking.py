# Q1. Banking System (Finance Domain)
# Design a BankAccount class.
# Methods to think about:
# • withdraw money (object method)
# • deposit money (object method)
# • display account details (object method)
# • update minimum balance (class method)

class BankAccount:
    bname='UBI'
    ifsc_code='UBINO505326'
    branch='Korutla'
    min_balance=10000

    def __init__(self,name,accountno,pan,balance,phone):
        self.name=name
        self.accountno=accountno
        self.pan=pan
        self.balance=balance
        self.phone=phone

    def withdraw_money(self,amount):
        if self.balance>0 and amount<=self.balance and self.balance-amount>=BankAccount.min_balance:
            self.balance-=amount
        else:
            print("Invalid Withdrawal")

    def deposit_money(self,amount):
        if amount>0:
            self.balance+=amount 
        else:
            print("Invalid Deposit")

    def display(self):
        print(self.name,self.accountno,self.pan,self.balance,self.phone)
    
    @classmethod

    def minimum_balance(cls,new_balance):
        if new_balance>0:
            cls.min_balance=new_balance

c1=BankAccount("Manyasri","13579086","ABCDEFGH",50000,"9440009098")
c2=BankAccount("Deeksha","24681357","MNOPQRST",62000,"9676091933")

c1.display()
c1.withdraw_money(8000)
c1.display()
c2.deposit_money(5000)
c2.display()

BankAccount.minimum_balance(20000)

c1.display()
c1.withdraw_money(10)
c1.display()