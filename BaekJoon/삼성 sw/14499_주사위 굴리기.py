import sys

input = sys.stdin.readline

N, M, y, x, K = map(int, input().split())

g = []
for _ in range(N):
    g.append(list(map(int, input().split())))

dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # 1: 밑면 6: 윗면

dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]  # 동 서 북 남

opers = list(map(int, input().split()))


def is_inside(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False


def value_check(y, x):
    if g[y][x] == 0:
        g[y][x] = dice[1]
    else:
        dice[1] = g[y][x]
        g[y][x] = 0
    print(dice[6])


for oper in opers:
    if oper == 1:  # 동
        if is_inside(y + dy[oper], x + dx[oper]):
            tmp = dice[1]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = tmp

            y, x = y + dy[oper], x + dx[oper]
            value_check(y, x)

    elif oper == 2:  # 서
        if is_inside(y + dy[oper], x + dx[oper]):
            tmp = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = tmp

            y, x = y + dy[oper], x + dx[oper]
            value_check(y, x)

    elif oper == 3:  # 북
        if is_inside(y + dy[oper], x + dx[oper]):
            tmp = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            dice[5] = tmp

            y, x = y + dy[oper], x + dx[oper]
            value_check(y, x)

    elif oper == 4:  # 남
        if is_inside(y + dy[oper], x + dx[oper]):
            tmp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = dice[2]
            dice[2] = tmp

            y, x = y + dy[oper], x + dx[oper]
            value_check(y, x)
