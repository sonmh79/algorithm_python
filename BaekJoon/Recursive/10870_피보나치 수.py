# DYNAMIC PROGRAMMING - 메모이제이션
import sys
n = int(sys.stdin.readline())

d = [0] * (n+1)

def f(x):
    
    if x <= 1:
        return x
    
    if x == 2:
        return 1
    
    if d[x]:
        return d[x]
    
    d[x] = f(x-1) + f(x-2)
    
    return d[x]

print(f(n))