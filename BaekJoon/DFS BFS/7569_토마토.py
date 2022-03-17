import sys
from collections import deque

input = sys.stdin.readline

M,N,H = map(int,input().split())

visited = []
trip = deque()
dx, dy, dh = [1,0,-1,0,0,0], [0,1,0,-1,0,0],[0,0,0,0,1,-1]

d = {}
for h in range(H):
    d[h] = {}
    for i in range(N):
        d[h][i] = list(map(int,input().split()))
        for j in range(M):
            if d[h][i][j] == 1:
                trip.append((h,i,j))


def bfs(trip):
    while trip:
        h,i,j = trip.popleft()
        for k in range(6):
            nx,ny,nh = i + dx[k], j + dy[k], h + dh[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H:
                if d[nh][nx][ny] == 0:
                    d[nh][nx][ny] = d[h][i][j] + 1
                    trip.append((nh,nx,ny))

    t = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if d[h][i][j] == 0:
                    return -1
                t = max(t,d[h][i][j])
    return t - 1
    
print(bfs(trip))
