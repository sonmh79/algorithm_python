import sys

"""
    1. 체스판을 순회하며 시작점을 잡는다.
    2. 시작점으로부터 가로, 세로 길이가 8 8 이 가능한지 확인한다.
    3. 가능하다면 그 시작점으로부터 8X8만큼 탐색한다.
    4. 단, 탐색 시 가로 세로 모두 2의 간격을 두고 탐색하며 한 번에 2X2 크기 만큼 확인한다.
    5. 왼쪽 상단이 B일 경우로 가정하며, W일 경우일 때와 비교하여 최소로 수정할 수 있는 값을 리턴한다. (W일 경우 = 64 - 좌상단이 B일 경우)
    6. 탐색이 모두 끝나고 각 점에서 수정해야하는 개수들의 최솟값 리턴
"""

r,c = map(int,sys.stdin.readline().split())

board = []
for _ in range(r):
    board.append(sys.stdin.readline().rstrip("\n"))

ans = []

def check_color(x,y):
    cnt = 0
    for i in range(x,x+8,2):
        for j in range(y,y+8,2):
            if board[i][j] != "B":
                cnt +=1
            if board[i+1][j] != "W":
                cnt += 1
            if board[i][j+1] != "W":
                cnt += 1
            if board[i+1][j+1] != "B":
                cnt += 1
    return min(cnt, 64-cnt)

for i in range(r):
    for j in range(c):
        if r-i >= 8 and c-j >= 8:
            ans.append(check_color(i,j))

print(min(ans))