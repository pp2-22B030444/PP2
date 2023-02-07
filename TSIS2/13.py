a=str(input())

l=[]
for i in range(len(a)):
    if a[i] not in l:
        l.append(a[i])
c=0
for j in l:
    for i in range(len(a)):
        if a[i]==j:
            c+=1
    print(j,c)        
    c=0        