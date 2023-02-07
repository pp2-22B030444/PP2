def f(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
f(1000)        