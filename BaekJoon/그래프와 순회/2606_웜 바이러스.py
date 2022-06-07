import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
t = int(input())
d = defaultdict(list)

for _ in range(t):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

visited = []
trip = [1]
def bfs(trip):

    while trip:
        node = trip.pop(0)
        if node not in visited:
            visited.append(node)
            trip += d[node]

bfs(trip)
print(len(visited)-1)

"""
    bfs로 1번과 연결된 모든 노드들을 탐색한다.
"""