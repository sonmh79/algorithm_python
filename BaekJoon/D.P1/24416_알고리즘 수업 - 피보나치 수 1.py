import sys

input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)
d[1] = 1
d[2] = 1

cnt = 0
def fibonacci(n):
    for i in range(3,n+1):
        global cnt
        cnt += 1
        d[i] = d[i-1] + d[i-2]
    print(d[n],cnt)

fibonacci(n)