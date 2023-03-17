#import os
import re
data=open("data.txt","r")

def delete(d):
    pattern=re.compile("[co]")
    r=re.sub(pattern,"",d)
    yield r
    
# for d in data:
#     s=delete(d)
#     print(next(s))

s=delete(data.read())
print(next(s))
