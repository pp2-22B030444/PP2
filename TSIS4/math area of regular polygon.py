from math import tanh
def area_of_regular_polygon(n,s):
    area=n*(s**2)/(4*tanh(180/n))
    return int(area)

n=int(input('Input number of sides: '))
s=int(input('Input the length of a side: '))
print('The area of the polygon is:',area_of_regular_polygon(n,s))