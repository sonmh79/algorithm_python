import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

maze = []

for _ in range(N):
    maze.append(input())

n,m = N-1,M-1
answer = []
visited = []
trip = deque([(0,0,1)])
cnt = 1

def bfs(trip):
    while trip:
        i,j,cnt = trip.popleft()

        if i == N-1 and j == M-1:
            answer.append(cnt)

        elif maze[i][j] == "1" and (i,j) not in visited:
            visited.append((i,j))
            if 0 <= i+1 < N and 0 <= j < M:
                trip.append((i+1,j,cnt+1))
            if 0 <= i < N and 0 <= j+1 < M:
                trip.append((i,j+1,cnt+1))
            if 0 <= i-1 < N and 0 <= j < M:
                trip.append((i-1,j,cnt+1))
            if 0 <= i < N and 0 <= j-1 < M:
                trip.append((i,j-1,cnt+1))

bfs(trip)
print(min(answer))

"""
    최적 경로 탐색을 위해 dfs보다는 bfs가 효율적이다.
    이미 방문한 노드를 유의하며 검사해야한다.
"""