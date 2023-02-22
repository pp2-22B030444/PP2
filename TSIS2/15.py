l=[(1,2), (2,3), (3,7), (4,16)]

for idx,val in enumerate(l):
       mult=1
       for v in val:
              mult *=v
       l[idx]=mult

print(l)       
