a = str(input())

l = []
for i in range(len(a)):
    if a[i] not in l:
        l.append(a[i])
count = 0
for let in l:
    for i in range(len(a)):
        if let == a[i]:
            count += 1
    print(let, count)
    count = 0