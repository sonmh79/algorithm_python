import sys
from collections import deque, defaultdict
input = sys.stdin.readline
N,M = map(int,input().split())

snake_and_ladder = defaultdict(int)
visited = defaultdict(int)
for _ in range(N+M):
    s,e = map(int,input().split())
    snake_and_ladder[s] = e

def bfs(node):
    q = deque()
    q.append((node,0))
    visited[node] = 1
    while q:
        n,cnt = q.popleft()
        for i in [1,2,3,4,5,6]:
            next_move = n+i
            if next_move > 100 or visited[next_move]:
                continue
            if next_move == 100:
                return cnt + 1
            visited[next_move] = 1
            if snake_and_ladder[next_move]:
                q.append((snake_and_ladder[next_move],cnt + 1))
            else:
                q.append((next_move,cnt + 1))

print(bfs(1))