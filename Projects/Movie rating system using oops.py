class movie_rating:
    def __init__(self,movie_name,rating=None,reviews=None):
        self.movie_name=movie_name
        self.rating=[]
        self.reviews=[]
    def give_rating(self,new_rating,review=""):
        self.rating.append(new_rating)
        self.reviews.append(f"review given :{new_rating} - {review}")
        print(f"rating given to {self.movie_name} :{new_rating}")

    def average_rating(self):
        if self.rating:
            avg=sum(self.rating)/len(self.rating)
            print(f"average rating for {self.movie_name} :{avg}")
        else:
            print(f"No ratings for {self.movie_name} yet.")
    def display_reviews(self):
        print(f"reviews for {self.movie_name}".center(20,"-"))
        for reviews in self.reviews:
            print(reviews)
    def overall_review(self,movie_condition=None):
        self.movie_condition=[]
        for reviews in self.reviews:
            if any(keyword in reviews for keyword in ["great", "good", "amazing", "incredible"]):
                self.movie_condition.append("positive review")
            elif any(keyword in reviews for keyword in ["bad", "terrible", "awful", "disappointing"]):
                self.movie_condition.append("negative review")
            elif any(keyword in reviews for keyword in ["average", "mediocre", "okay", "fine"]):
                self.movie_condition.append("neutral review")
            else:
                self.movie_condition.append("neutral review")
        if sum(self.rating)/len(self.rating)>2 and self.movie_condition.count("positive review")==self.movie_condition.count("negative review"):
            d="mixed reviews"
        else:
            d=max(set(self.movie_condition), key=self.movie_condition.count)
        print(f"overall review for {self.movie_name} :{d}")
    def is_family_friendly(self):
        if any(keyword in self.reviews for keyword in ["child abuse", "Nudity", "violence", "strong language"]):
            print(f"{self.movie_name} is not family friendly")
        else:
            print(f"{self.movie_name} is family friendly")
a=movie_rating("eagle movie")
a.give_rating(5,"strong language and violence")    
a.give_rating(4,"average movie")
a.give_rating(3,"bad movie")
a.give_rating(1,"average movie and contains violence")
a.give_rating(2,"average movie and countains violence")
a.average_rating()
a.display_reviews()
a.overall_review()
a.is_family_friendly()


