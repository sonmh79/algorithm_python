import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M,R = map(int,input().split())
g = defaultdict(list)

for _ in range(M):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

ans = [0] * (N+1)
visited = defaultdict(int)
visited[R] = 1
ans[R] = 1
cnt = 1
def dfs(n):

    for node in sorted(g[n]):
        if not visited[node]:
            visited[node] = 1
            global cnt
            cnt += 1
            ans[node] = cnt
            dfs(node)
dfs(R)
for i in range(1,N+1):
    print(ans[i])
