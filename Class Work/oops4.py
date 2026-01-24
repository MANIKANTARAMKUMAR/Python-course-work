class watsapp:
    def status(self):
        print("you can post status")
class watsappV2(watsapp):
    def statuswithmusic(self):
        super().status()
        print("you can post status with music")
abhinav=watsapp()
abhinav.status()
abhinav=watsappV2()
abhinav.statuswithmusic()
abhinav.status()