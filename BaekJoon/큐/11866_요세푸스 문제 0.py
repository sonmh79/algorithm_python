import sys
from collections import defaultdict

input = sys.stdin.readline
d = defaultdict(int)

N,K = map(int,input().split())

nums = list(range(1,N+1))
ans = []

i = 0
cnt = 0
while len(ans) < N:
    i = i%N
    if nums[i] != 0:
        cnt += 1
    
    if cnt == K:
        cnt = 0
        ans.append(nums[i])
        nums[i] = 0
    
    i += 1

res = "<"
for a in ans:
    res += str(a)
    res += ", "

res = res.rstrip(", ")
print(res + ">")