def generates_the_squares(n):
    l=[]
    for i in range(1,n):    
        l.append(i**2)   
    return l

a=int(input())
print(generates_the_squares(a))        