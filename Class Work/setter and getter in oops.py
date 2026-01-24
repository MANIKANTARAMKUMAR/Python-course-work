class instagram:
    def __init__(self,username,password,profilepicture):
        self.username=username
        self.__password=password
        self._profilepicture=profilepicture
    @property
    def profilepicture(self):
        return self._profilepicture
    @profilepicture.setter
    def profilepicture(self,newprofilepicture):
        self._profilepicture=newprofilepicture

    def getpwd(self):
        return self.__password
    def setpwd(self,newpwd):
        self.__password=newpwd

abhinav=instagram("abhinav","abhi123","public",)
vishnu=instagram("vishnu","vishnu123","private")
print(f"Userinfo\n{abhinav.username}\n{abhinav.getpwd()}\n{abhinav.profilepicture}")
print(f"Userinfo\n{vishnu.username}\n{vishnu.getpwd()}\n{vishnu.profilepicture}")
print(abhinav.username)
abhinav.profilepicture="friends"
print(abhinav.profilepicture)
print(f"Userinfo\n{abhinav.username}\n{abhinav.getpwd()}\n{abhinav.profilepicture}")


class instagramV1:
    def postphoto(self,photo):
        print(f"photo posted:{photo}")
    def postvideo(self,video):
        print(f"video posted:{video}")
class instagramV2(instagramV1):
    def postreels(self,reels):
        print(f"reels posted:{reels}")
abhinav=instagramV2()
abhinav.postphoto("photo1.jpg")
abhinav.postvideo("video1.mp4")
abhinav.postreels("reels1.mp4")
abhinav=instagramV1()
abhinav.postphoto("photo2.jpg")
abhinav.postvideo("video2.mp4")
"""abhinav.postreels("reels2.mp4")"""#only instagramV2 class has postreels method
# abhinav.postreels("reels2.mp4") # This will raise an AttributeError
class instagramV3:
    def note(self):
        print("you can add note ")
    def highlites(self):
        print("you can add highlites")
print("abhinav -instagramV3")
abhinav=instagramV3()
abhinav.note()
abhinav.highlites()
print("vishnu -instagramV2")
vishnu=instagramV2()
vishnu.postphoto("photo3.jpg")
vishnu.postreels("reels3.mp4")
vishnu.highlites() # This will raise an AttributeError
"""vishnu.note()""" # This will raise an AttributeError
# vishnu.note() # This will raise an AttributeError