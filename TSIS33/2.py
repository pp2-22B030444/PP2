def fact(n):
    i=1
    factorial=1
    while i<=n:
        factorial*=i
        i+=1
    return factorial
a=int(input())
print(fact(a))