import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split())

visited = []
trip = deque()
dx, dy = [1,0,-1,0], [0,1,0,-1]

d = {}
for i in range(N):
    d[i] = list(map(int,input().split()))
    for j in range(M):
        if d[i][j] == 1:
            trip.append((i,j))


def bfs(trip):
    while trip:
        i,j = trip.popleft()
        for k in range(4):
            nx,ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if d[nx][ny] == 0:
                    d[nx][ny] = d[i][j] + 1
                    trip.append((nx,ny))

    t = 0
    for i in range(N):
        for j in range(M):
            if d[i][j] == 0:
                return -1
            t = max(t,d[i][j])
    return t - 1
    
print(bfs(trip))

"""
    움직일 수 있는 상하좌우를 리스트로 만든 후 for문을 돌려 코드를 간결하게 할 수 있다.
    그래프를 탐색하며 걸리는 시간을 합산한다.
"""