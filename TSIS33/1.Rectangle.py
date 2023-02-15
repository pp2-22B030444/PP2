class Shape():
    def area(self):
        return 0

class rec(Shape):
    def __init__(self,l,w): # ИНИЦИАЛИЗАЦИЯ ИЛИ ПРОСТО НАЧАЛО РАБОТЫ КЛАССА ИЛИ ФУНКЦИИ
        self.l = l
        self.w = w
    def area(self):
        return self.w*self.l
        
a=int(input())
b=int(input())       
rect=rec(a,b)
print(rect.area())
print(Shape().area())