from collections import defaultdict
# Buttom-up Tabulation

d = defaultdict(int)

def f(n):

    d[0] = 0
    d[1] = 1

    for i in range(2,n+1):
        d[i] = d[i-1] + d[i-2]
    
    return d[n]

print(f(5))
    
    