import sys

input = sys.stdin.readline

T = int(input())
answer = []

for _ in range(T):
    M,N,K = map(int,input().split())

    d = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        i,j = map(int,input().split())
        d[i][j] = 1
    
    visited = []

    def dfs(i,j):

        if i < 0 or i > M-1 or j < 0 or j > N-1:
            return
        
        if d[i][j] == 1 and (i,j) not in visited:
            visited.append((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

    cnt = 0
    for i in range(M):
        for j in range(N):
            if d[i][j] == 1 and (i,j) not in visited:
                dfs(i,j)
                cnt += 1
    answer.append(cnt)

for a in answer:
    print(a)