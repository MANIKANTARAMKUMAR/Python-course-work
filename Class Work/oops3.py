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
class instagramV3:
    def note(self):
        print("you can add note ")
    def highlites(self):
        print("you can add highlites")
class autoscroll():
    def autoscroll(self):
        print("you can autoscroll")
class summarize():
    def summarize(self):
        print("you can summarize")
class instagramV4(instagramV3,autoscroll,summarize):
    def repost(self):
        print("you can repost")









        
print("abhinav -instagramV3")
abhinav=instagramV3()
abhinav.note()
abhinav.highlites()
print("vishnu -instagramV2")
vishnu=instagramV2()
vishnu.postphoto("photo3.jpg")
vishnu.postreels("reels3.mp4")
instagramV4().autoscroll()
instagramV4().summarize()
instagramV4().repost()