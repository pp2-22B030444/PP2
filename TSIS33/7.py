

def count(n):
    c=0
    for i in n:       
        if type(i)==float:    
            c+=1
    print(c)
count([1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22])
            