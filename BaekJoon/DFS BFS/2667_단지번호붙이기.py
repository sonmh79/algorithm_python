import sys

input = sys.stdin.readline

N = int(input())
d = []
for _ in range(N):
    row = input().rstrip("\n")
    d.append(row)

visited = []
answer = []

def dfs(i,j):

    if i < 0 or i > N-1 or j < 0 or j > N-1:
        return
    
    if d[i][j] != "1" or (i,j) in visited:
        return

    visited.append((i,j))
    dfs(i+1,j)
    dfs(i,j+1)
    dfs(i-1,j)
    dfs(i,j-1)

for i in range(N):
    for j in range(N):
        if d[i][j] == "1" and (i,j) not in visited:
            pre_len = len(visited)
            dfs(i,j)
            cur_len = len(visited)
            answer.append(cur_len-pre_len)

print(len(answer))
for n in sorted(answer):
    print(n)

"""
    dfs를 통해 "1"인 노드 탐색
    예외 처리 해주기
"""