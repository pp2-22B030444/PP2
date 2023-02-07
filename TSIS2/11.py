n = int(input())
d = {}
for i in range(n):
    name, grade = input().split()
    grade = int(grade)
    if name in d:
        d[name].append(grade)
    else:
        d[name] = [grade]
for name in d:
    avg = sum(d[name]) / len(d[name])
    print(name, int(avg))