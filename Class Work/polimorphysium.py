class hotstar():
    def __init__(self,name):
        self.name=name
    def playvideo(self):
        print("adds are there in free version")
        print("welcome to hotstar")
        print("quality of video is 1080p")
        print("speed of video is normal")
    def login(self):
        print(f"welcome {self.name} to hotstar")
    def searchmovie(self,movie):
        print(f"you searched for {movie}")
    def menu(self):
        print("1.home\n2.movies\n3.series\n4.kids")
    def addtofavorites(self,movie):
        print(f"{movie} added to favorites")
class premiumhotstar(hotstar):
    def __init___(self,name):
        self.name=name
    def playvideo(self):
        print("you can watch 4k movies")
        print("welcome to premium hotstar")
        print("quality of video is 4k")
        print("speed of video is high speed")
    def login(self):
        print(f"welcome {self.name} to premium hotstar")
    def downloadmovie(self,movie):
        print(f"{movie} downloaded successfully")
abhinav=hotstar("abhinav")
abhinav.playvideo()
abhinav.login()
abhinav.searchmovie("avengers")
abhinav.menu()
abhinav.addtofavorites("avengers")
print("-----premium hotstar-----")
vishnu=premiumhotstar("vishnu")
vishnu.playvideo()
vishnu.login()
vishnu.searchmovie("ironman")
vishnu.menu()
vishnu.addtofavorites("ironman")
vishnu.downloadmovie("ironman")
# abhinav.downloadmovie("avengers") # This will raise an AttributeError