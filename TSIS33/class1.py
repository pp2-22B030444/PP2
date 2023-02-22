a=[1,2,3,4,5]
c=[]
b=input()
if b=='map * 3':
    for i in a:
        c.append(i*3)
    print(c)
if b=='filter > 3':
    for i in a:
        if i>3:
            c.append(i)
    print(c)
if b=='progression +':
    d=0
    for i in a:
        d+=i
        c.append(d)
    print(c)
if b=='fold +':
    d=0
    for i in a:
       d+=i
    c.append(d)
    print(c)
