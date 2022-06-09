import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
dx = [1,-1]
N,K = map(int,input().split())
h = [(0,N)]
visited = defaultdict(int)
while h:
    t,x = heapq.heappop(h)
    if x == K:
        print(t)
        break

    jx = x * 2
    if not visited[jx] and abs(K - jx) < abs(K - x):
        visited[jx] = 1
        heapq.heappush(h, (t, jx))

    for i in range(2):
        nx = x+dx[i]
        nt = t+1
        if not visited[nx] and nx >= 0:
            visited[nx] = 1
            heapq.heappush(h,(nt,nx))