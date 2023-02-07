class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        self.length = length

    def area(self):
        return self.length**2

a=int(input())
Asqr =Square(a)
print(Asqr.area())      # prints 25 as given argument
print(Square().area())  # prints zero as default area