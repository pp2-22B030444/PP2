import re
data=open("Create Words.txt","r")

def delete(d):
    pattern=re.compile(r'\W*\b\w{1,3}\b')
    r=re.sub(pattern,"",d)
    return r

s=delete(data.read())
print(s)
