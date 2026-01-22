class Flipcart:
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