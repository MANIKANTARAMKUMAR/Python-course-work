"""a="37"
sum=0
l=len(a)
for i in a :
    sum+=int(i)**l
if sum==int(a):
    print("armstrong")
else:
    print("not armstrong")



"""
"""
num = int(input("Enter a number: "))
for i in range (num):
    for j in range (i):
        print(end=" ")
print("#",end=" ")"""

"""n = int(input("Enter a number: "))
for i in range (n):
    if i<=n//2:
        print("* "*(i+1))
    else:
        print("* " *(n-i))

"""
"""A=int(input("Enter a number: "))
for i in range (A):
    for j in range (A):
        if i==0 or i==A//2 or j==0 or j==A-1 or i==A-1:
            print("* ",end=" ")
        else:
            print(" ",end=" ")         
a=int(input("enter a number:"))
for i in range (a):
    for j in range (a):
        if i==0 or j==0 or i==a-1 or j==a:
            print("* ",end=" ")
        print()
 """
"""       
#positional arguments
def display(name , age, place ,roll):
    print(f"Name: {name} \nAge: {age} \nPlace: {place} \nRoll: {roll}")

name=input("Enter your name:")
age=int(input("Enter your age:"))
place=input("Enter your place:")
roll=int(input("Enter your roll number:"))

display(name=name, age=age, place=place, roll=roll)
display(name=age, age=place, place=roll, roll=name)
display(name=name, age=roll, place=place, roll=age)
"""
"""
#default arguments
def display(name, age, place, roll,status="single"):
    print(f"Name: {name} \nAge: {age} \nPlace: {place} \nRoll: {roll} \nStatus: {status}\n")

display("Alice", 20, "New York", 101)
display("Bob", 22, "Los Angeles", 102, status="gay")
"""
"""
def display(**names):
    for i in names:
        print(f'{i}: {names[i]}')
    print("----------------")

display(name="sai", age="22", place="hyd", roll="101")
display(name="ram", age="23", place="delhi", roll="102", status="single")
display(name="ravi", age="24", place="mumbai", roll="103", status="married", job="engineer")
"""

"""
#global and local variables
def display(name):
    name="hello"
    print(f"Inside function: {name}")

name="ram"
display(name)
print(f"Outside function: {name}")
"""

"""

def display():
    name="hello"
    print(f"Inside function: {name}")

name="ram"
display()
print(f"Outside function: {name}")

def display():
    global name
    name="hello"
    print(f"Inside function: {name}")


display()
print(f"Outside function: {name}")

"""

"""
def display(course):
    print(f"starting course: {course}")

    def inner():
        course = "python"
        print(f"inside inner function of {course} course")

    inner()

    print(f"ending course: {course}")

course="java"
display(course)

"""
"""
def display(course):
    print(f"starting course: {course}")

    def inner():
        nonlocal course
        course = "python"
        print(f"inside inner function of {course} course")

    inner()

    print(f"ending course: {course}")

course="java"
display(course)
"""
"""
a=int(input("enter a number:"))
for i in range (1,a+1):
    for j in range (1,a+1):
        print(f"{i}X{j}={i*j}\n")
"""
"""
def display(n):
    n=n.copy()
    n.append(5)
    print("Inside function:",n)
n=[1,2,3,4]
display(n)
print("Outside function:",n)
"""

"""
def display(n):
    n.strip()
    for i in range(1,len(n)+1):
        k=n[0:i]
        print(k)
n="hello"
display(n)
"""
"""
def display(n,a):
    n.strip()
    for i in range(0,len(n),a):
        k=n[i:i+a]
        print(k)
n="helloworld"
display(n,3)
"""
"""
def shoot(bullets):
    while bullets > 0:
        print("Bang!")
        bullets -= 1
    else:
        print("No bullets left!")
    return bullets
shoot(10)
"""
'''
def wish(name):
    return f"Hello, {name}!"
print(wish("Alice"))
print(wish("Bob"))

wish1=lambda name: f"Hello, {name}!"
print(wish1("Alice"))
'''
'''
greatest=lambda a,b: a if a>b else b
print (greatest(10,20))

sum1=lambda a,b,c: a+b+c
print(sum1(10,20,30))
'''
'''
def square(n):
    b=[]
    for i in range(1,n+1):
        if i%2==0:
            pass
        else:
            b.append(i**2)
    print(b)
square(7)
k=list(filter(lambda x:x%2!=0,range(1,8)))



a=[1,0,0,0,0,2,4,5,7,6,0,1,0]
b=[]
for i in a:
    if i!=0:
        b.append(i)
print(b)

s="helloworld"
v="aeiou"
n=list(filter(lambda s:s in v,s))
print(n)

l=[1,0,0,2,3,0,4,0,5]
n=list(filter(lambda i:i!=0,l))
print(n)
'''
'''from functools import reduce
l=[1,2,3,4,5]
s=reduce(lambda a,b:a+b,l)
print(s)'''
'''
from functools import reduce
names=["sai","ram","ravi","raju"]
s=reduce(lambda a,b:a+" "+b,names)
print(s)

a=int(input("enter a number:"))
b=[]
for i in range (1,a+1):
    if i%2==0:
        pass
    else:
        b.append(i**2)
print(b)
'''
'''
a=int(input("enter a number:"))
b=""
for i in range (1,a+1):
    for j in range(1,i+1):
        b+=str(i+j)
    print(b) 
'''
'''
import ATM
u_PIN=int(input("Enter your PIN:"))
if ATM.validate_PIN(u_PIN):
    print("PIN validation successful.")
    while True:
        print("/n/n/n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. view Transaction History")
        print("5. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            ATM.check_balance()
        elif choice==2:
            amount=float(input("Enter amount to deposit:"))
            ATM.deposit_money(amount)
        elif choice==3:
            amount=float(input("Enter amount to withdraw:"))
            ATM.withdraw_money(amount)
        elif choice==4:
            ATM.view_transaction_history()
        elif choice==5:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid PIN. Access denied.")

'''
'''
from ATM import login,check_balance,deposit_money,withdraw_money,view_transaction_history,validate_PIN
u_PIN=int(input("Enter your PIN:"))
if ATM.validate_PIN(u_PIN):
    print("PIN validation successful.")
    while True:
        print("/n/n/n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. view Transaction History")
        print("5. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            check_balance()
        elif choice==2:
            amount=float(input("Enter amount to deposit:"))
            deposit_money(amount)
        elif choice==3:
            amount=float(input("Enter amount to withdraw:"))
            withdraw_money(amount)
        elif choice==4:
            view_transaction_history()
        elif choice==5:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid PIN. Access denied.")
'''
'''
from ATM import *
u_PIN=int(input("Enter your PIN:"))
if ATM.validate_PIN(u_PIN):
    print("PIN validation successful.")
    while True:
        print("/n/n/n")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. view Transaction History")
        print("5. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            ATM.check_balance()
        elif choice==2:
            amount=float(input("Enter amount to deposit:"))
            ATM.deposit_money(amount)
        elif choice==3:
            amount=float(input("Enter amount to withdraw:"))
            ATM.withdraw_money(amount)
        elif choice==4:
            ATM.view_transaction_history()
        elif choice==5:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid PIN. Access denied.")
'''
'''
import random 
random.seed(10)
print((random.randint(00,123)))
print(random.uniform(1,10))
names=["sai","ram","ravi","raju"]
print(random.choice(names))
print(random.choices(names,k=2))
random.shuffle(names)
print(names)
print(random.sample(names,2))
'''
'''
a=list(map(int,input("enter numbers:").split(',')))
b=[]
for i in a:
    if i%2==0:
        b.append(i**2)
print(b)
'''

'''
import datetime
now=datetime.datetime.now()
print("Current date and time:",now)

from datetime import date,time,datetime
today=date.today()
print("Today's date:",today)
print("Current year:",today.year)
print("current month",today.month)
print("current day",today.day)
print("current weekday:",today.weekday())
print("current is iso weekday:",today.isoweekday())
print("current iso format:",today.isoformat())

'''
'''
from datetime import date,time,datetime
now=datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.timetuple())
print(now.isoformat())
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%I:%M :%S %p"))
print(now.strftime("%A, %b, %d, %Y"))
print(now.strftime("%I:%M:%S %p"))

'''


from datetime import date,time,datetime,timedelta
now=datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.timetuple())
print(now.isoformat())
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%I:%M :%S %p"))
print(now.strftime("%A, %b, %d, %Y"))
print(now.strftime("%I:%M:%S %p"))