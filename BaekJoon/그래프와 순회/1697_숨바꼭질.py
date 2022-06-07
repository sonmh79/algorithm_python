import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int,input().split())

def move(x):
    return [x-1, x+1, 2*x]

d = [0] * 100001
d[N] = 1
trip = deque()
trip.append(N)
def bfs(trip):

    while trip:
        x = trip.popleft()
        if x == K:
            return d[x] -1 
        
        for dx in move(x):
            nx = dx
            if 0 <= nx <= 100000:
                if d[nx] == 0:
                    d[nx] = d[x] + 1
                    trip.append(nx)
        

print((bfs(trip)))

"""
    최단 경로 찾기에는 dfs가 최고 ??
    캐시 메모리를 만들어 직접 매핑하면 빠르게 탐색 가능
"""