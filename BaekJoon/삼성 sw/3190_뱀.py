import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
apples = [[0 for _ in range(N)] for _ in range(N)]  # 사과 그래프
for _ in range(K):
    y, x = map(int, input().split())
    apples[y - 1][x - 1] = 1
L = int(input())  # 뱀의 방향 변환 횟수
snake_move_info = deque([])
for _ in range(L):
    y, x = input().split()
    snake_move_info.append((int(y), x))
dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
idx = 0
t = 0
snake = deque([[0, 0]])

while True:

    if snake_move_info:
        if t == snake_move_info[0][0]:
            _, d = snake_move_info.popleft()
            if d == "L":
                idx -= 1
            else:
                idx += 1
                idx %= 4

    dy, dx = dyx[idx]

    t += 1

    y, x = snake[0]
    ny, nx = y + dy, x + dx

    if 0 <= ny < N and 0 <= nx < N:

        if [ny, nx] in snake:
            break

        if apples[ny][nx]:  # 사과 먹기
            snake.appendleft([ny, nx])
            apples[ny][nx] = 0

        else:  # 사과 없음
            snake.appendleft([ny, nx])
            snake.pop()

    else:  # 벽에 부딪힘
        break

print(t)
for i in range(-10, 10):
    print(i % 4)
