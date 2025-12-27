"""l=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(l): 
    print (l[i])
    i+=1


"""
'''chances=5
stored_password="admin123"
while chances>0:
    password=input("Enter your password: ")
    if password==stored_password:
        print("Login Successful!")
        break
    else:
        chances-=1
        print(f"Incorrect Password! You have {chances} chances left.")
else:
    print("incorrect password! No chances left. Account locked.")
    '''
'''a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i==13:
        print(i)
        break
else:
    print("not found")
    '''

a="37"
sum=0
l=len(a)
for i in a :
    sum+=int(i)**l
if sum==int(a):
    print("armstrong")
else:
    print("not armstrong")


