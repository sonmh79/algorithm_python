import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
oq = deque(list(map(int,input().split())))

dq = deque(range(1,N+1))
cnt = 0
while oq:
    n = oq.popleft()
    if n == dq[0]:
        dq.popleft()
    else:
        l,r = 0,0
        for i in range(1,len(dq)):
            if n == dq[i]:
                r = i
                break
        for i in range(1,len(dq)):
            if n == dq[-i]:
                l = i
                break
        
        if l < r:
            for _ in range(l):
                dq.appendleft(dq.pop())
            cnt += l
        else:
            for _ in range(r):
                dq.append(dq.popleft())
            cnt += r
        dq.popleft()
print(cnt)