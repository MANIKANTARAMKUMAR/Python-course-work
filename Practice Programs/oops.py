'''class Book:
    def __init__(self,title,author,price):
        self.title =title
        self.author=author
        self.price=price
    def display(self):
        print(f"title :{self.title}\nAuthor :{self.author}\nPrice :₹{self.price}")
a=Book("python","me",230)
a.display() 

'''

from itertools import count


class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_average_salary(self):
        self.average_salary=self.base_salary*12
        print(f"average salary :₹{self.average_salary}")

a=Employee("john",2000)
a.calculate_average_salary()    

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        avg=sum(self.marks)/len(self.marks)
        print(f"average marks of {self.name} :{avg}")
        return "pass" if all(mark>=49 for mark in self.marks) else "fail"
    
a=student("john",[80,90,70 ])
b=student("doe",[50,60,49])
print(f"{a.name} : {a.result()}")
print(f"{b.name} : {b.result()}")
class Bankaccount:
    def __init__(self,balance=0,history=None):
        self.balance=balance
        self.history=[]
    def deposite(self,amount):
        self.balance+=amount
        self.history.append(f"deposited :₹{amount}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=amount
            self.history.append(f"withdrawn :₹{amount}")
        else:
            print(f"insufficient balance :₹{self.balance}")
    def display_history(self):
        print("Transaction History".center(10,"-"))
        for transations in self.history:
            print(transations)
    
        



a=Bankaccount()
a.deposite(1000)
a.withdraw(500)
a.withdraw(600) 
a.deposite(2000)
a.withdraw(100)
a.display_history()


class Car:
    def __init__(self,reading,brand):
        self.reading=reading
        self.brand=brand
    def drive(self,distance):
        self.reading+=distance
        print(f"{self.brand} driven for {distance} km")

    def odometer_reading(self):
        print(f"odometer reading :{self.reading} km")
a=Car(1000,"toyota")
a.drive(200)
a.odometer_reading()    

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
a=movie_rating("eagle movie")
a.give_rating(5,"amazing movie")    
a.give_rating(4,"great movie")
a.give_rating(3,"bad movie")
a.give_rating(1,"bad movie")
a.give_rating(2,"average movie")
a.average_rating()
a.display_reviews()
a.overall_review()




