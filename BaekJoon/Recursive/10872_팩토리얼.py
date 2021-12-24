# 1. 기본 풀이
import sys
n = int(sys.stdin.readline())

num = 1
for i in range(1,n+1):
    num *= i
    
print(num)

# 2. 재귀를 이용한 풀이
import sys
n = int(sys.stdin.readline())

def f(x):
    
    if x == 0 or x == 1:
        return 1
    
    return x*f(x-1)

print(f(n))