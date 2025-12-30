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
'''A=int(input("Enter a number: "))
for i in range (A):
    for j in range (A):
        if i==0 or i==A//2 or j==0 or j==A-1 or i==A-1:
            print("* ",end=" ")
        else:
            print(" ",end=" ")
            '''
a=int(input("enter a number:"))
for i in range (a):
    for j in range (a):
        if i==0 or j==0 or i==a-1 or j==a:
            print("* ",end=" ")
        print()