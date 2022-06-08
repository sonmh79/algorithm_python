import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V,E = map(int,input().split()) # V: 정점의 개수, E: 간선의 개수
K = int(input()) # K: 시작 정점의 번호

g = defaultdict(list)
for _ in range(E):
    u,v,w = map(int,input().split())
    g[u].append((w,v))

h = g[K]
answer = ["INF" for _ in range(V+1)]
answer[K] = 0
heapq.heapify(h)
while h:
    cost,node = heapq.heappop(h)
    if answer[node] == "INF":
        answer[node] = cost
        for next_cost,next_node in g[node]:
            if answer[next_node] == "INF":
                heapq.heappush(h,(cost+next_cost,next_node))

for i in range(1,V+1):
    print(answer[i])
