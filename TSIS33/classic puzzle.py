def solve(numheads, numlegs):
    ns = "No solutions!"
    for i in range(numheads):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns, ns
a=int(input())  
b=int(input())  
print(solve(a,b))  
import ownes
ownes.ounes