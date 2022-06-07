import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())
RG = {1: "R", 0: "G"}

def dfs(n,c):
    cur_color = RG[c]
    next_color = RG[1-c]

    for next_node in g[n]:
        if color[next_node] == None:
            color[next_node] = next_color
        else:
            if color[next_node] == cur_color:
                return "NO"
        
        if not visited[next_node]:
            visited[next_node] += 1
            res = dfs(next_node,1-c)
            if res == "NO":
                return "NO"
                    

    return "YES"
                

answer = []
for _ in range(K):
    V,E = map(int,input().split())
    visited = defaultdict(int)
    g = defaultdict(list)
    color = [None] * (V+1)
    color[1] = RG[1]
    flag = True
    for _ in range(E):
        a,b = map(int,input().split())
        g[a].append(b)
        g[b].append(a)

    for i in range(1,V+1):
        if not visited[i]:
            visited[i] += 1
            res = dfs(i,1)
            if res == "NO":
                flag = False
                break
    if flag:
        answer.append("YES")
    else:
        answer.append("NO")

for a in answer:
    print(a)

"""
    DFS로 연결된 그래프의 노드들을 탐색하며 빨강과 초록색을 번갈아가며 칠하기
    연결 안된 그래프가 있을 수 있기 때문에 체크해준다.
"""