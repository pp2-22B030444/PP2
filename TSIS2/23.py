n = int(input())
d = {}
f=[]
for i in range(n):
    key, value = input().split()
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]
#for key in d:
    if key=='str':
        f.append(d[key])
    if key=='bool':
        if d[key]=='True':
            f.sort(reverse=False)
        else:
            f.sort(reverse=True)
    if key==d[key]:
        f.append(d[key])        
print(f)           
   