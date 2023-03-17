def factorial(n):
    pr=1
    for i in range(1,n+1):
        pr=pr*i
        yield pr


s=factorial(10)

for i in range(1,11):
    print(next(s))
