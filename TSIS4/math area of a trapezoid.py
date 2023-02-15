#import math 
def area_of_a_trapezoid(a,b,c):
    area=((b+c)/2)*a
    return area

a=int(input('Height: '))
b=int(input('Base, first value: '))
c=int(input('Base, second value: '))
print('Expected Output:',area_of_a_trapezoid(a,b,c))