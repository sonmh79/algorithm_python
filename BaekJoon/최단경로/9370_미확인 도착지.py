import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

INF = int(1e7)

def bfs(start, end):
    if start == end:
        return 0

    q = [(0,start)]
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    while q:
        c, node = heapq.heappop(q)

        if node == end:
            return c

        for nc, nn in graph[node]:
            if distance[nn] > c+nc: # whattt
                distance[nn] = c + nc
                heapq.heappush(q, (c + nc, nn))

    return distance[end]


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

    ans = []
    for _ in range(t):
        x = int(input())

        route1 = bfs(s, g) + bfs(g,h) + bfs(h, x)
        route2 = bfs(s, h) + bfs(h,g) + bfs(g, x)

        min_route = bfs(s, x)
        if (route1 == min_route) or (route2 == min_route):
            ans.append(x)

    print(*sorted(ans))
