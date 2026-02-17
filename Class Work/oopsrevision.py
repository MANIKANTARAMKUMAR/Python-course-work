class book:
    def __init__(self,name ,author,price):
        self.name=name
        self.author=author
        self.price=price
    def display(self):
        print("name",self.name)
        print("author",self.author)
        print("price",self.price)
a=book("python","me",230)
a.display()

class employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_anual_salary(self):
        self.anual_salary=self.base_salary*12
        print("anual salary",self.anual_salary)

a=employee("john",2000)
a.calculate_anual_salary()


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        avg=sum(self.marks)/len(self.marks)
        for mark in self.marks:
            if mark>=avg:
                print("pass")
            else:
                print("fail")
a=student("john",[80,90,70])
a.result()

'''
class BankAccount:
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(self.balance)
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(self.balance)
        else:
            print("insufficient balance")
a=BankAccount(12345,"john",1000)
a.deposit(500)
a.withdraw(800)


'''