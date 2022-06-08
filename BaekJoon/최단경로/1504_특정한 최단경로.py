import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N,E = map(int,input().split()) # N: 정점의 개수, E: 간선의 개수

g = defaultdict(list)
for _ in range(E):
    u,v,w = map(int,input().split())
    g[u].append((w,v))
    g[v].append((w,u))
v1,v2 = map(int,input().split())
INF = int(1e7)
def dijkstra(start,end):
    if start == end:
        return 0
    dist = [INF for _ in range(N+1)]
    dist[start] = 0
    h = [(0,start)]
    while h:
        cost,node = heapq.heappop(h)

        for c,n in g[node]:
            if c+cost < dist[n]:
                dist[n] = c+cost
                heapq.heappush(h,(c+cost,n))
    return dist[end]


cost1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N)
cost2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,N)
answer = min(cost1,cost2)
if answer < INF:
    print(answer)
else:
    print(-1)