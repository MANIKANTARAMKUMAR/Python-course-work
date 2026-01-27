a=int(input("Enter a number: "))
if len(str(a))==4:
    b=sum(map(int,str(a)))
    c=sum(map(int,str(b)))
    d= sum(map(int,str(c)))
    print(d)
else:
    print("input is not a 4 digit number")