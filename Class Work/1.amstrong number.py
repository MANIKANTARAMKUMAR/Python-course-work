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
