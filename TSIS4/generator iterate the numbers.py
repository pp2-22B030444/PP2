def iterate_the_numbers(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            print(i,end=' ')
            
a=int(input())
iterate_the_numbers(a)