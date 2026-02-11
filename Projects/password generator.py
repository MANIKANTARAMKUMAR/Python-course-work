import random
upprt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower= "abcdefghijklmnopqrstuvwxyz"
num='0123456789'
symbols='!@#$%^&*()_+-=`~'
all_char=upprt+lower+num+symbols
lenth=int(input("enter lenth of password :"))
password=''.join(random.sample(all_char,lenth))
print('password  :  ',password)