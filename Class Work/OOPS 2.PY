'''class Flipcart:
    def userinfo(self,name,password,mobilenumber):
        self.name=name
        self.password=password
        self.mobilenumber=mobilenumber
        print(f"Userinfo\n{name}\n{password}\n{mobilenumber}")
ajay=Flipcart()
vijay=Flipcart()

ajay.userinfo("ajay","ajay123",9876543210)
vijay.userinfo("vijay","vijay123",8765432109)


class Flipcart:
    discount=10
    @classmethod
    def getdiscount(cls):
        print(f"the discount is {cls.discount}%")
    @staticmethod
    def banner():
        print("welcome to flipcart")
    def __init__(self,name,password,mobilenumber):
        self.name=name
        self.password=password
        self.mobilenumber=mobilenumber
        print(f"Userinfo\n{name}\n{password}\n{mobilenumber}")
ajay=Flipcart("ajay","ajay123",9876543210)
vijay=Flipcart("vijay","vijay123",8765432109)
Flipcart.getdiscount()
Flipcart.banner()
'''
class instagram:
    def __init__(self,username,password,profilepicture):
        self.username=username
        self.__password=password
        self._profilepicture=profilepicture
    def getpwd(self):
        return self.__password
    def setpwd(self,newpwd):
        self.__password=newpwd



abhinav=instagram("abhinav","abhi123","public")
vishnu=instagram("vishnu","vishnu123","private")
print("Userinfo\n{self.username}\n{self.__password}\n{self._profilepicture}")
print(abhinav.username)
print(vishnu.username)
print(abhinav._profilepicture)
print(vishnu._profilepicture)
abhinav.__password="newpass"
print(abhinav.__password)
abhinav.username="newuser"
print(abhinav.username)
print(f"before password:{abhinav.getpwd()}")
abhinav.setpwd("newpass123")
print(f"after password:{abhinav.getpwd()}")
