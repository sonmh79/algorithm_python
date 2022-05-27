from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def spread(y, x, ng):
    dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if ng[ny][nx] == 0:
                ng[ny][nx] = 2
                spread(ny, nx, ng)


def count_zero(ng):
    res = 0
    for l in ng:
        res += l.count(0)
    return res


def dfs(cnt):
    if cnt == 3:
        ng = deepcopy(g)
        for i in range(N):
            for j in range(M):
                if ng[i][j] == 2:
                    spread(i, j, ng)
        res = count_zero(ng)
        global ans
        ans = max(ans, res)
        return

    for y in range(N):
        for x in range(M):
            if g[y][x] == 0:
                g[y][x] = 1
                dfs(cnt + 1)
                g[y][x] = 0


dfs(0)
print(ans)
