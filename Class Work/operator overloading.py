class Number:
    def __init__(self,number):
        self.number=number
    def __add__(self,other):
        return self.number+other.number
    def __sub__(self,other):
        return self.number-other.number
    def __mul__(self,other):
        return self.number*other.number
    def __floordiv__(self,other):
        return self.number//other.number
    def __gt__(self,other):
        return self.number>other.number
    def __it__(self,other):
        return self.number<other.number
    def __eq__(self,other):
        return self.number==other.number
    def __str__(self):
        return str(self.number)

