import sys

input = sys.stdin.readline

N = int(input())

g = []
for _ in range(N):
    g.append(list(map(int, input().split())))


def move(y, x, my, mx, visited):

    while 0 <= y + my < N and 0 <= x + mx < N and not visited[y][x]:
        y += my
        x += mx
    return y, x


ans = 0


def dfs(graph, cnt):

    global ans
    for i in range(N):
        for j in range(N):
            ans = max(ans, graph[i][j])
    if cnt == 6:
        return

    visited = [[0 for _ in range(N)] for _ in range(N)]
    merged = [[0 for _ in range(N)] for _ in range(N)]
    new_g = [[0 for _ in range(N)] for _ in range(N)]
    dy, dx = -1, 0  # Up
    for y in range(N):
        for x in range(N):
            if graph[y][x]:
                ny, nx = move(y, x, dy, dx, visited)
                if visited[ny][nx]:
                    if not merged[ny][nx] and new_g[ny][nx] == graph[y][x]:
                        new_g[ny][nx] += graph[y][x]
                        merged[ny][nx] = 1
                        continue
                    else:
                        ny -= dy
                        nx -= dx
                visited[ny][nx] = 1
                new_g[ny][nx] = graph[y][x]
    if new_g != graph:
        dfs(new_g, cnt + 1)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    merged = [[0 for _ in range(N)] for _ in range(N)]
    new_g = [[0 for _ in range(N)] for _ in range(N)]
    dy, dx = 0, -1  # Left
    for x in range(N):
        for y in range(N):
            if graph[y][x]:
                ny, nx = move(y, x, dy, dx, visited)
                if visited[ny][nx]:
                    if not merged[ny][nx] and new_g[ny][nx] == graph[y][x]:
                        new_g[ny][nx] += graph[y][x]
                        merged[ny][nx] = 1
                        continue
                    else:
                        ny -= dy
                        nx -= dx
                visited[ny][nx] = 1
                new_g[ny][nx] = graph[y][x]
    if new_g != graph:
        dfs(new_g, cnt + 1)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    merged = [[0 for _ in range(N)] for _ in range(N)]
    new_g = [[0 for _ in range(N)] for _ in range(N)]
    dy, dx = 1, 0  # Down
    for y in range(N - 1, -1, -1):
        for x in range(N):
            if graph[y][x]:
                ny, nx = move(y, x, dy, dx, visited)
                if visited[ny][nx]:
                    if not merged[ny][nx] and new_g[ny][nx] == graph[y][x]:
                        new_g[ny][nx] += graph[y][x]
                        merged[ny][nx] = 1
                        continue
                    else:
                        ny -= dy
                        nx -= dx
                visited[ny][nx] = 1
                new_g[ny][nx] = graph[y][x]
    if new_g != graph:
        dfs(new_g, cnt + 1)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    merged = [[0 for _ in range(N)] for _ in range(N)]
    new_g = [[0 for _ in range(N)] for _ in range(N)]
    dy, dx = 0, 1  # Right
    for x in range(N - 1, -1, -1):
        for y in range(N):
            if graph[y][x]:
                ny, nx = move(y, x, dy, dx, visited)
                if visited[ny][nx]:
                    if not merged[ny][nx] and new_g[ny][nx] == graph[y][x]:
                        new_g[ny][nx] += graph[y][x]
                        merged[ny][nx] = 1
                        continue
                    else:
                        ny -= dy
                        nx -= dx
                visited[ny][nx] = 1
                new_g[ny][nx] = graph[y][x]
    if new_g != graph:
        dfs(new_g, cnt + 1)


dfs(g, 1)
print(ans)
