a= [100, "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktau"]
l1=[]
l2=[]
l4=[]
l3=[]
for i in range(len(a)):
    if type(a[i])==int: 
        l1.append(a[i])  
    if type(a[i])==str:
        l2.append(a[i]) 
    if type(a[i])==float:
        l4.append(a[i])    
    if type(a[i])==bool:
        l3.append(a[i]) 
for i in range(1):
    print(l1)
    print(l2)
    print(l4)
    print(l3) 
    