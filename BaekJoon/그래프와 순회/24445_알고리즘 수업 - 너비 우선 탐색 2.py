import sys
from collections import defaultdict, deque
input = sys.stdin.readline

g = defaultdict(list)
N,M,R = map(int,input().split())
for _ in range(M):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

ans = [0] * (N+1)
cnt = 1
visited = defaultdict(int)
visited[R] = 1
ans[R] = 1

q = deque([R])
while q:
    node = q.popleft()
    for n in sorted(g[node],reverse=True):
        if not visited[n]:
            visited[n] = 1
            cnt += 1
            ans[n] = cnt
            q.append(n)

for i in range(1,N+1):
    print(ans[i])