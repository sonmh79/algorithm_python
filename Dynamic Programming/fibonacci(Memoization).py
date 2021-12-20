from collections import defaultdict
# Top-down Memoization

d = defaultdict(int)

def f(n):

    if n == 1:
        return 1
    
    if n == 0:
        return 0

    if d[n]: # 저장되어 있는 결과를 불러온다.
        return d[n]

    d[n] = f(n-1) + f(n-2) # 계산 결과를 저장한다.
    return d[n]

print(f(10))
    
    