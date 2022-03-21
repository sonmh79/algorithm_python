import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int,input().split())

d = []
dx, dy = [1,0,-1,0], [0,1,0,-1]
for _ in range(N):
    d.append(list(map(int,input().rstrip("\n"))))

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

trip = deque()
trip.append((0,0,1))
def bfs(trip):

    while trip:
        x,y,cnt = trip.popleft()

        if (x,y) == (N-1,M-1):
            return visited[cnt][x][y] + 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if d[nx][ny] == 0 and not visited[cnt][nx][ny]:
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                    trip.append((nx,ny,cnt))
                
                elif d[nx][ny] == 1 and not visited[cnt][nx][ny]:
                    if cnt == 1:
                        visited[cnt-1][nx][ny] = visited[cnt][x][y] + 1
                        trip.append((nx,ny,cnt-1))
    
    return -1

print(bfs(trip))

"""
    visited를 2차원으로 나눈다.(벽 뚫기 찬스를 사용했을 때와 안 사용했을 경우 2가지)
    일찍 도착했지만 찬스를 이미 사용하여 더 나아갈 수 없을 경우와 늦게 도착하지만 찬스가 남아 더 나아갈 수 있는 경우 문제를 해결할 수 있다.
"""