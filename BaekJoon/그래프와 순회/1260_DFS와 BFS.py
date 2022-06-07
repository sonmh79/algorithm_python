import sys
from collections import defaultdict

input = sys.stdin.readline

n,m,start = map(int,input().split())
d = defaultdict(list)

for i in range(m):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)

def dfs(s,visited):

    if s not in visited:
        visited.append(s)
        for node in sorted(d[s]):
            if node not in visited:
                dfs(node,visited)
    return visited

trip = [start]
visited = []
def bfs(trip):

    while trip:
        node = trip.pop(0)
        if node not in visited:
            visited.append(node)
            for n in sorted(d[node]):
                if n not in visited:
                    trip.append(n)
    return visited
    
print(*dfs(start,[]))
print(*bfs(trip))