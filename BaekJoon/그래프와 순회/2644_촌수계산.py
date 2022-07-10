import heapq
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
x,y = map(int,input().split())
m = int(input())

visited = [0]*(n+1)
g = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

heap = []
heapq.heappush(heap,(0,x))
visited[x] = 1
def bfs():
    while heap:
        cnt,p = heapq.heappop(heap)
        if p == y:
            return cnt
        for i in g[p]:
            if not visited[i]:
                visited[i] = 1
                heapq.heappush(heap,(cnt+1,i))
    return -1
print(bfs())
