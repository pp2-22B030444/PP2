import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return 2
poin1=Point(1,2)
point2=Point(2,3)
point3=Point(4,5)
# a=int(input())
# b=int(input())
# point=point(a,b)
print(poin1.show())
print(point2.dist(pt=poin1))
