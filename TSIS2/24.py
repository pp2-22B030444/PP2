f = lambda x: x * x
f(5)
print(f(5))
f = lambda x, y: x * y
print(f(5, 2))
f = lambda: True
print(f())
def f(x):
    return x * x

def modify_list(L, fn):
    for idx, v in enumerate(L):
        L[idx] = fn(v)

L = [1, 3, 2]
modify_list(L, f)
print(L)