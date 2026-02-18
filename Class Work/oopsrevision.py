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

class car:
    def __init__(self,brand,model,year):
        self.brand=brand
    def start (self):
        print(f"{self.brand}  is starting")
class vehicle(car):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)
    def start(self):
        print(f"{self.brand} is starting with a roar")
    def show_details(self):
        print(f"brand: {self.brand} ")

a=vehicle("ford","mustang",2020)
a.start()
a.show_details()
b=car("toyota","camry",2019)
b.start()



class Account:
    def __init__(self):
       self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
        print(self.__balance)
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print(self.__balance)
        else:
            print("insufficient balance")
a=Account()
a.deposit(1000)
a.withdraw(210)

from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        self.amount=amount
        print(f"paying {self.amount}")
        
    def UPI(self,amount):
        self.amount=amount
        print(f"paying {self.amount} through UPI") 
class CreditCard(payment):
    def pay(self,amount):
        super().pay(amount)
    def UPI(self,amount):
        super().UPI(amount)
a=CreditCard()
a.pay(1000)
a.UPI(500)


class notification:
    @abstractmethod
    def notification(self):
        pass
class email(notification):
    def notify(self):
        print("sending email notification")
class sms(notification):
    def notify(self):
        print("sending sms notification")
a=email()
a.notify()  
b=sms()
b.notify()

class transportation:
    def __init__(self,mode):
        self.mode=mode
    def travel(self):
        print(f"traveling by {self.mode}")


class employee:
    def developper(self):
        print("developing software")
class manager(employee):
    def manage(self):
        super().developper()
        print("managing team")     
class testing(employee):
    def test(self):
        super().developper()
        print("testing software") 

a=manager()
a.manage()
b=testing()
b.test()    

