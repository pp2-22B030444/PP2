a=int (input("Insert a:"))
num=str(a)
list1 =[]
for i in num:
    list1.append(i)

list1.sort(reverse=True)

s=""
for i in list1:
    s+=i
num1=int(s)
print(num1)    