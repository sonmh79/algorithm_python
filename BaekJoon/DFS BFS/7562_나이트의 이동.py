import sys
from collections import deque
input = sys.stdin.readline


dx, dy = [2,2,1,1,-1,-1,-2,-2], [1,-1,2,-2,2,-2,1,-1]

def dfs(trip, l, target):
    
    while trip:
        x,y= trip.popleft()
        if (x,y) == target:
            return d[x][y]


        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if d[nx][ny] == 0:
                    d[nx][ny] = d[x][y] + 1
                    trip.append((nx,ny))

ans = []
T = int(input())
for _ in range(T):

    l = int(input())
    sx,sy = map(int,input().split())
    tx,ty = map(int,input().split())
    d = [[0 for _ in range(l)] for _ in range(l)]
    trip = deque()
    trip.append((sx,sy))
    ans.append(dfs(trip, l, (tx, ty)))

for a in ans:
    print(a)

"""
    체스 말의 이동 가능한 루트를 사전에 정의 후 bfs로 탐색
    if ~ in visited 로 검사하는 것보다 딕셔너리로 그래프를 직접 검색하는게 빠름
"""