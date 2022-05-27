from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
visited = [[0 for _ in range(M)] for _ in range(N)]
dy, dx = [1, -1, 0], [0, 0, 1]
ans = 0


def dfs(y, x, cnt, tet_sum):
    if cnt == 4:
        global ans
        ans = max(ans, tet_sum)
        return

    for i in range(3):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = 1
            if cnt == 2:
                dfs(y, x, cnt + 1, tet_sum + board[ny][nx])
            dfs(ny, nx, cnt + 1, tet_sum + board[ny][nx])
            visited[ny][nx] = 0


for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        dfs(y, x, 1, board[y][x])
        visited[y][x] = 0
print(ans)
