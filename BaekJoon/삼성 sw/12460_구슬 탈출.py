import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = []
visited = [
    [[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)
]

for i in range(n):
    row = list(input().rstrip("\n"))
    if "R" in row:
        Ry, Rx = i, row.index("R")
    if "B" in row:
        By, Bx = i, row.index("B")
    g.append(row)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

q = deque()
q.append((Ry, Rx, By, Bx, 1))
visited[Ry][Rx][By][Bx] = 1
g[Ry][Rx] = "."
g[By][Bx] = "."


def move(y, x, my, mx):
    steps = 0
    while g[y + my][x + mx] != "#" and g[y][x] != "O":
        y += my
        x += mx
        steps += 1
    return y, x, steps


def bfs(q):
    while q:
        Ry, Rx, By, Bx, cnt = q.popleft()
        if cnt > 10:
            print(-1)
            return

        for i in range(4):
            Rny, Rnx, R_steps = move(Ry, Rx, dy[i], dx[i])
            Bny, Bnx, B_steps = move(By, Bx, dy[i], dx[i])

            if g[Bny][Bnx] == "O":
                continue
            if g[Rny][Rnx] == "O":
                print(cnt)
                return

            if Rny == Bny and Rnx == Bnx:
                if R_steps > B_steps:
                    Rny -= dy[i]
                    Rnx -= dx[i]
                else:
                    Bny -= dy[i]
                    Bnx -= dx[i]

            if not visited[Rny][Rnx][Bny][Bnx]:
                visited[Rny][Rnx][Bny][Bnx] = 1
                q.append((Rny, Rnx, Bny, Bnx, cnt + 1))
    print(-1)


bfs(q)
